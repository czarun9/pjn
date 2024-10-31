import random

import spacy
import os
import matplotlib.pyplot as plt
from collections import Counter
import pandas as pd
from nltk import word_tokenize
from sklearn.feature_extraction.text import TfidfVectorizer
from wordcloud import WordCloud
from morfeusz2 import Morfeusz

nlp = spacy.load("pl_core_news_sm")
morfeusz = Morfeusz()


def read_book_to_corpus(folder_path):
    corpus = []
    for file_name in os.listdir(folder_path):
        if file_name.endswith('.txt'):
            file_path = os.path.join(folder_path, file_name)
            with open(file_path, 'r', encoding='utf-8') as file:
                text = file.read()
                corpus.append((file_name, text))
    return corpus


def process_corpus_with_spacy(corpus):
    processed_corpus = []
    for title, text in corpus:
        doc = nlp(text)
        tokens_info = [
            (token.text, token.lemma_, token.pos_, token.tag_)
            for token in doc
            if token.is_alpha and not token.is_stop
        ]
        processed_corpus.append((title, tokens_info))
    return processed_corpus


def analyze_pos_and_tag(corpus):
    pos_counts = {}
    tag_counts = {}

    for title, text in corpus:
        doc = nlp(text)
        pos_freq = Counter([token.pos_ for token in doc])
        tag_freq = Counter([token.tag_ for token in doc])

        pos_counts[title] = dict(pos_freq)
        tag_counts[title] = dict(tag_freq)

    return pos_counts, tag_counts



def noun_counts_by_lemma(processed_corpus):
    noun_counts_per_book = {}

    for title, tokens_info in processed_corpus:
        noun_counts = Counter()
        for token in tokens_info:
            if token[2] == 'NOUN':
                lemma = token[1]
                noun_counts[lemma] += 1
        noun_counts_per_book[title] = noun_counts

    return noun_counts_per_book


def visualize_counts(counts, title, xlabel):
    for book_title, count_data in counts.items():
        sorted_counts = dict(sorted(count_data.items(), key=lambda x: x[1], reverse=True))

        limited_counts = dict(list(sorted_counts.items())[:50])

        plt.figure(figsize=(12, 6))
        labels, values = zip(*limited_counts.items())

        plt.bar(labels, values, color='skyblue')
        plt.title(f"{title} dla: {book_title}")
        plt.xlabel(xlabel)
        plt.ylabel("Częstość")

        plt.xticks(rotation=90, fontsize=10)
        plt.yticks(fontsize=10)

        plt.tight_layout()
        plt.show()

        print(f"50 najpopularniejszych {xlabel} dla: {book_title}")
        for label, value in limited_counts.items():
            print(f"{label}: {value}")
        print("\n")


def create_tfidf_matrix(noun_counts):
    documents = []

    for title, counts in noun_counts.items():
        doc = ' '.join([f"{lemma} " * count for lemma, count in
                        counts.items()])
        documents.append(doc.strip())

    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(documents)
    return pd.DataFrame(tfidf_matrix.toarray(), columns=vectorizer.get_feature_names_out(), index=noun_counts.keys())


def plot_wordcloud_per_book(noun_counts):
    for title, counts in noun_counts.items():
        wordcloud = WordCloud(width=800, height=400, background_color='white').generate_from_frequencies(counts)

        plt.figure(figsize=(10, 5))
        plt.imshow(wordcloud, interpolation='bilinear')
        plt.axis('off')
        plt.title(f"Chmura Tagów dla Książki: {title}")
        plt.show()


def extract_ambiguous_words(corpus):
    ambiguous_words = {}
    for title, text in corpus:
        words = word_tokenize(text)
        for word in words:
            analyses = morfeusz.analyse(word)
            if len(analyses) > 1:
                analyses_str = [f"{analysis[2][1]} ({analysis[2][2]})" for analysis in analyses]
                ambiguous_words[word] = analyses_str
    return ambiguous_words


def display_random_ambiguous_words(ambiguous_words):
    sampled_words = random.sample(list(ambiguous_words.items()), min(100, len(ambiguous_words)))

    print("Tabela losowych 100 niejednoznacznych słów:\n")
    for word, analyses in sampled_words:
        print(f"Słowo: {word}")
        print("Możliwe analizy:")
        for analysis in analyses:
            print(f" - {analysis}")
        print("\n")


def find_subjects_and_verbs(corpus, n_subjects=10):
    subjects_verbs = {}

    for title, text in corpus:
        doc = nlp(text)
        subjects = []

        for sent in doc.sents:
            for token in sent:
                if token.dep_ in ("nsubj", "nsubjpass") and token.pos_ == "NOUN":
                    subject = token.text
                    verb = token.head.text
                    subjects.append(subject)

                    subjects_verbs[subject] = verb

                if len(subjects) >= n_subjects:
                    break
            if len(subjects) >= n_subjects:
                break

        break

    return subjects_verbs


if __name__ == "__main__":
    folder_path = '../resources/books'
    corpus = read_book_to_corpus(folder_path)

    processed_corpus = process_corpus_with_spacy(corpus)

    pos_counts, tag_counts = analyze_pos_and_tag(corpus)

    visualize_counts(pos_counts, "Częstość występowania części mowy", "Części mowy")
    visualize_counts(tag_counts, "Częstość występowania tagów", "Tagi")

    noun_counts = noun_counts_by_lemma(processed_corpus)
    for book_title, counts in noun_counts.items():
        visualize_counts({book_title: counts}, "Częstość występowania rzeczowników (lematy)", "Rzeczowniki")

    ambiguous_words = extract_ambiguous_words(corpus)
    display_random_ambiguous_words(ambiguous_words)
    print("/n")

    tfidf_matrix = create_tfidf_matrix(noun_counts)
    print(tfidf_matrix)
    plot_wordcloud_per_book(noun_counts)
    subjects_verbs = find_subjects_and_verbs(corpus)

    print("Rzeczowniki pełniące funkcję podmiotu i związane z nimi czasowniki:")
    for subject, verb in subjects_verbs.items():
        print(f"Podmiot: {subject}, Orzeczenie: {verb}")