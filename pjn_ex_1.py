import os
import nltk
from nltk import sent_tokenize, word_tokenize
from nltk.corpus import stopwords

nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('stopwords')


def load_stopwords(filepath):
    with open(filepath, 'r', encoding='utf-8') as file:
        stopwords = file.read().splitlines()
    return set(stopwords)


stopwords_file_path = os.path.join('resources', 'polish.stopwords.txt')
stopwords = load_stopwords(stopwords_file_path)


def preprocess_text(text):
    tokens = word_tokenize(text)

    processed_tokens = [
        token.lower() for token in tokens
        if token.isalnum() and token.lower() not in stopwords
    ]

    return processed_tokens


folder_path = 'resources'

corpus = []


def read_book_to_corpus(corpus):
    for file_name in os.listdir(folder_path):
        if file_name.endswith('.txt'):
            file_path = os.path.join(folder_path, file_name)
            with open(file_path, 'r', encoding='utf-8') as file:
                text = file.read()
                corpus.append(text)
    return corpus;


corpus = read_book_to_corpus(corpus)
processed_corpus = [preprocess_text(document) for document in corpus]

print("Przetworzony dokument:", processed_corpus[0][:50])

