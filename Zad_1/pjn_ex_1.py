import os
import nltk
from nltk import word_tokenize
import matplotlib.pyplot as plt
from collections import Counter
from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.decomposition import PCA

nltk.download('punkt')
nltk.download('punkt_tab')


def load_stopwords(filepath):
    with open(filepath, 'r', encoding='utf-8') as file:
        stopwords = file.read().splitlines()
    return set(stopwords)


stopwords_file_path = os.path.join('../resources', 'polish.stopwords.txt')
stopwords = load_stopwords(stopwords_file_path)


def read_book_to_corpus(corpus):
    for file_name in os.listdir(folder_path):
        if file_name.endswith('.txt'):
            file_path = os.path.join(folder_path, file_name)
            with open(file_path, 'r', encoding='utf-8') as file:
                text = file.read()
                corpus.append(text)
    return corpus


def preprocess_text(text):
    tokens = word_tokenize(text)

    processed_tokens = [
        token.lower() for token in tokens
        if token.isalpha() and token.lower() not in stopwords
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
        plt.figure(figsize=(10, 8))
        plt.bar(words[:30], counts[:30])
        plt.xticks(rotation=90)
        plt.title(f'Częstości słów w dokumencie: {document_labels[i]}')
        plt.ylabel('Częstość')
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
        line_y = (frequencies[s - 1] / line_x) ** s
        plt.loglog(line_x, line_y, linestyle='--', color='red', label=f'Linia Zipfa (s={s})')

        plt.title(f'Prawo Zipfa dla dokumentu: {document_labels[i]}')
        plt.xlabel('Ranga')
        plt.ylabel('Częstość')
        plt.grid(True)
        plt.legend()
        plt.show()


def create_tfidf_matrix(corpus):
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform([' '.join(doc) for doc in processed_corpus])
    return pd.DataFrame(tfidf_matrix.toarray(), columns=vectorizer.get_feature_names_out())


def reduce_dimensions_pca(tfidf_matrix, n_components=2):
    pca = PCA(n_components=n_components)
    return pca.fit_transform(tfidf_matrix)


def plot_2d_scatter(matrix_2d, labels=None):
    plt.figure(figsize=(10, 6))
    plt.scatter(matrix_2d[:, 0], matrix_2d[:, 1], c='blue', marker='o')

    if labels is not None:
        for i, label in enumerate(labels):
            plt.annotate(label, (matrix_2d[i, 0], matrix_2d[i, 1]))

    plt.title('Redukcja wymiarowości dokumentów do 2D')
    plt.xlabel('Składowa 1')
    plt.ylabel('Składowa 2')
    plt.grid(True)
    plt.show()


folder_path = '../resources/books'
document_labels = [
    "Mała syrenka",
    "Calineczka",
    "Dziewczynka z zapałkami",
    "Królowa śniegu",
    "W pustyni i w puszczy"
]
corpus = []

if __name__ == "__main__":
    corpus = read_book_to_corpus(corpus)
    processed_corpus = [preprocess_text(document) for document in corpus]

    word_counts = calculate_word_counts(processed_corpus)

    print("Wykresy częstości (Counter):")
    plot_word_frequencies(word_counts)

    print("Prawo Zipfa dla wybranych dokumentów:")
    plot_zipf_law(word_counts)

    print("Utwórz matrycę TfIdf")
    tfidf_df = create_tfidf_matrix(processed_corpus)
    print(tfidf_df)

    print("Obliczanie macierzy podobieństwa kosinusowego")
    cosine_sim_matrix = cosine_similarity(tfidf_df)
    print(cosine_sim_matrix)

    print("Redukcja wymiarowości PCA")
    reduced_tfidf_matrix = reduce_dimensions_pca(tfidf_df)
    print(reduced_tfidf_matrix)

    plot_2d_scatter(reduced_tfidf_matrix, labels=document_labels)
