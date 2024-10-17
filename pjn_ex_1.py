import os
import nltk
from nltk import word_tokenize
from nltk.corpus import stopwords
import matplotlib.pyplot as plt
from collections import Counter
from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd
import numpy as np

nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('stopwords')


def load_stopwords(filepath):
    with open(filepath, 'r', encoding='utf-8') as file:
        stopwords = file.read().splitlines()
    return set(stopwords)


stopwords_file_path = os.path.join('resources', 'polish.stopwords.txt')
stopwords = load_stopwords(stopwords_file_path)


def read_book_to_corpus(corpus):
    for file_name in os.listdir(folder_path):
        if file_name.endswith('.txt'):
            file_path = os.path.join(folder_path, file_name)
            with open(file_path, 'r', encoding='utf-8') as file:
                text = file.read()
                corpus.append(text)
    return corpus;


def preprocess_text(text):
    tokens = word_tokenize(text)

    processed_tokens = [
        token.lower() for token in tokens
        if token.isalnum() and token.lower() not in stopwords
    ]

    return processed_tokens


def calculate_word_counts(corpus):
    word_counts = []
    for doc in corpus:
        counts = Counter(doc)
        word_counts.append(counts)
    return word_counts


def plot_word_frequencies(word_counts):
    for i, counts in enumerate(word_counts):
        sorted_word_counts = counts.most_common()

        words, counts = zip(*sorted_word_counts)
        plt.figure(figsize=(10, 5))
        plt.bar(words[:30], counts[:30])
        plt.xticks(rotation=90)
        plt.title(f'Częstości słów w dokumencie {i + 1} (Counter)')
        plt.show()


def plot_zipf_law(word_counts):
    for i, counts in enumerate(word_counts):
        sorted_word_counts = counts.most_common()
        ranks = range(1, len(sorted_word_counts) + 1)
        frequencies = [count for word, count in sorted_word_counts]

        plt.figure(figsize=(10, 5))
        plt.loglog(ranks, frequencies, marker=".", label='Dane')

        s = 1
        line_x = np.array(ranks)
        line_y = (frequencies[s-1] / line_x) ** s
        plt.loglog(line_x, line_y, linestyle='--', color='red', label=f'Linia Zipfa (s={s})')

        plt.title(f'Prawo Zipfa dla dokumentu {i + 1}')
        plt.xlabel('Ranga')
        plt.ylabel('Częstość')
        plt.grid(True)
        plt.legend()
        plt.show()


def create_tfidf_matrix(corpus):
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform([' '.join(doc) for doc in processed_corpus])
    return pd.DataFrame(tfidf_matrix.toarray(), columns=vectorizer.get_feature_names_out())


folder_path = 'resources/books'

corpus = []

corpus = read_book_to_corpus(corpus)
processed_corpus = [preprocess_text(document) for document in corpus]
word_counts = calculate_word_counts(processed_corpus)

print("Wykresy częstości (Counter):")
# plot_word_frequencies(word_counts)

print("Prawo Zipfa dla wybranych dokumentów:")
# plot_zipf_law(word_counts)

print("Utwórz matrycę TfIdf")
tfidf_df = create_tfidf_matrix(processed_corpus)

print(tfidf_df)
print(tfidf_df.head())
