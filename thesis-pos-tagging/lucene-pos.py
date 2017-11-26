# -*- coding: utf-8 -*-
import pymysql
import pymysql.cursors
from nltk.tokenize import RegexpTokenizer
from stop_words import get_stop_words
from nltk.stem.porter import PorterStemmer
from gensim import corpora, models
import gensim
from time import time
import spacy
import pandas as pd
import numpy as np
import en_core_web_sm
import json

start_time = time()

conn = pymysql.connect(host='localhost', user='root', password='password', db='Issue_Trackers', autocommit=True, use_unicode=True, charset="utf8")

cursor_1 = conn.cursor()
cursor_1.execute("SELECT * FROM lucene_rss_comments")

lucene_rss_list = list()

for row in cursor_1:
    lucene_rss_list.append(row[4])

for x in range(len(lucene_rss_list)):
    print(lucene_rss_list[i])

end_time = time()
time_taken = end_time - start_time

print("Total time taken in seconds: ", time_taken)
