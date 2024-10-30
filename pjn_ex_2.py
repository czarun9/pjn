import spacy
import os
import matplotlib.pyplot as plt
from collections import Counter

nlp = spacy.load("pl_core_news_sm")


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
            (token.text, token.lemma_, token.pos_, token.morph)
            for token in doc
            if token.is_alpha and not token.is_stop
        ]
        processed_corpus.append((title, tokens_info))
    return processed_corpus


def analyze_pos_and_morph(processed_corpus):
    pos_counts = {}
    morph_counts = {}

    for title, tokens_info in processed_corpus:
        pos_freq = Counter([token[2] for token in tokens_info])
        morph_freq = Counter([str(token[3]) for token in tokens_info])

        pos_counts[title] = dict(pos_freq)
        morph_counts[title] = dict(morph_freq)

    return pos_counts, morph_counts


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


if __name__ == "__main__":
    folder_path = 'resources/books'
    corpus = read_book_to_corpus(folder_path)

    processed_corpus = process_corpus_with_spacy(corpus)

    pos_counts, morph_counts = analyze_pos_and_morph(processed_corpus)

    visualize_counts(pos_counts, "Częstość występowania części mowy", "Części mowy")
    visualize_counts(morph_counts, "Częstość występowania klas morfologicznych", "Klasy morfologiczne")

    noun_counts = noun_counts_by_lemma(processed_corpus)
    for book_title, counts in noun_counts.items():
        visualize_counts({book_title: counts}, "Częstość występowania rzeczowników (lematy)", "Rzeczowniki")