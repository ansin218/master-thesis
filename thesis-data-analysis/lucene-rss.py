# -*- coding: utf-8 -*-
import pymysql
import pymysql.cursors
import random
from bs4 import BeautifulSoup
import nltk
from nltk import tokenize
from time import time
import re

start_time = time()

conn = pymysql.connect(host='localhost', user='root', password='password', db='master_thesis', autocommit=True, use_unicode=True, charset="utf8")
cursor_1 = conn.cursor()
cursor_2 = conn.cursor()
cursor_3 = conn.cursor()
cursor_4 = conn.cursor()
cursor_5 = conn.cursor()
cursor2 = conn.cursor()

cursor_1.execute("SELECT * FROM lucene_counter_rss WHERE count > 5 AND count <= 10")
cursor_2.execute("SELECT * FROM lucene_counter_rss WHERE count > 10 AND count <= 15")
cursor_3.execute("SELECT * FROM lucene_counter_rss WHERE count > 15 AND count <= 20")
cursor_4.execute("SELECT * FROM lucene_counter_rss WHERE count > 20 AND count <= 25")
cursor_5.execute("SELECT * FROM lucene_counter_rss WHERE count > 25 AND count <= 30")

lucene_rs_list_1 = list()
lucene_rs_list_2 = list()
lucene_rs_list_3 = list()
lucene_rs_list_4 = list()
lucene_rs_list_5 = list()

for row in cursor_1:
    lucene_rs_list_1.append(row[1])

for row in cursor_2:
    lucene_rs_list_2.append(row[1])

for row in cursor_3:
    lucene_rs_list_3.append(row[1])

for row in cursor_4:
    lucene_rs_list_4.append(row[1])

for row in cursor_5:
    lucene_rs_list_5.append(row[1])

print(len(lucene_rs_list_1))
print(len(lucene_rs_list_2))
print(len(lucene_rs_list_3))
print(len(lucene_rs_list_4))
print(len(lucene_rs_list_5))
total_len = len(lucene_rs_list_1) + len(lucene_rs_list_2) + len(lucene_rs_list_3) + len(lucene_rs_list_4) + len(lucene_rs_list_5)
print("Total Issues: ", total_len)

#random.shuffle(lucene_rs_list)
#final_list = lucene_rs_list[:100]

conn.close()

end_time = time()
time_taken = end_time - start_time

print("Total time taken in seconds: ", time_taken)
