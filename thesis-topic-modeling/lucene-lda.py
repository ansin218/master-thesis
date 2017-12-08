# -*- coding: utf-8 -*-
import pymysql
import pymysql.cursors
from nltk.tokenize import RegexpTokenizer
from stop_words import get_stop_words
from nltk.stem.porter import PorterStemmer
from nltk.stem.wordnet import WordNetLemmatizer
from gensim import corpora, models, utils
import gensim
from time import time

start_time = time()

conn = pymysql.connect(host='localhost', user='root', password='password', db='Issue_Trackers', autocommit=True, use_unicode=True, charset="utf8")

cursor_1 = conn.cursor()
cursor_1.execute("SELECT * FROM lucene_rss_comments")

lucene_rss_list = list()

for row in cursor_1:
    lucene_rss_list.append(row[4])

tokenizer = RegexpTokenizer(r'\w+')
en_stop = get_stop_words('en')
alphaList = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numList = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
customList1 = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
en_stop = en_stop + alphaList + numList

p_stemmer = PorterStemmer()
lmtzr = WordNetLemmatizer()

doc_set = lucene_rss_list

texts = []

for i in doc_set:

    raw = i.lower()
    tokens = tokenizer.tokenize(raw)
    stopped_tokens = [i for i in tokens if not i in en_stop]
    stemmed_tokens = [lmtzr.lemmatize(i) for i in stopped_tokens]
    texts.append(stemmed_tokens)

dictionary = corpora.Dictionary(texts)
corpus = [dictionary.doc2bow(text) for text in texts]
ldamodel = gensim.models.ldamodel.LdaModel(corpus, num_topics=20, id2word = dictionary, passes=20)

print(ldamodel.print_topics(20))

end_time = time()
time_taken = end_time - start_time

print("Total time taken in seconds: ", time_taken)
