import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
import pandas as pd
import string
import pickle

def PreProcessing(text):
    text = text.lower()

    tokens = word_tokenize(text)

    tokens = [token for token in tokens if token not in string.punctuation]

    stop_words = set(stopwords.words('english'))
    tokens = [token for token in tokens if token not in stop_words]

    stemmer = PorterStemmer()
    tokens = [stemmer.stem(token) for token in tokens]

    return tokens



pre_processed = []

data = pd.read_csv('imdb_top_1000.csv')

summaries = data['Overview']

for i in range(len(summaries)):
    pre_processed.append(PreProcessing(summaries[i]))


documents = [' '.join(doc) for doc in pre_processed]

vectorizer = TfidfVectorizer()

tf_idf_vectors = vectorizer.fit_transform(documents)

print('tf-idf vectors shape',tf_idf_vectors.shape)

cosine_similarities = cosine_similarity(tf_idf_vectors)

print('tf-idf vectors shape',cosine_similarities.shape)


with open('cosine_similarities.pickle', 'wb') as f:
    pickle.dump(cosine_similarities, f)


with open('TF-IDF-VECTORS.pickle', 'wb') as f:
    pickle.dump(tf_idf_vectors, f)


with open('MOVIES-TITLE.pickle', 'wb') as f:
    pickle.dump(data['Series_Title'], f)













# 'Poster_Link', 'Series_Title', 'Released_Year', 'Certificate',
#        'Runtime', 'Genre', 'IMDB_Rating', 'Overview', 'Meta_score', 'Director',
#        'Star1', 'Star2', 'Star3', 'Star4', 'No_of_Votes', 'Gross'],
#       dtype='object'