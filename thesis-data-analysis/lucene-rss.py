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

insert_cursor = conn.cursor()

cursor_1 = conn.cursor()
cursor_1.execute("SELECT * FROM lucene_counter_rss WHERE count > 5 AND count <= 10")
cursor_2 = conn.cursor()
cursor_2.execute("SELECT * FROM lucene_counter_rss WHERE count > 10 AND count <= 15")
cursor_3 = conn.cursor()
cursor_3.execute("SELECT * FROM lucene_counter_rss WHERE count > 15 AND count <= 20")
cursor_4 = conn.cursor()
cursor_4.execute("SELECT * FROM lucene_counter_rss WHERE count > 20 AND count <= 25")
cursor_5 = conn.cursor()
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

total_len = len(lucene_rs_list_1) + len(lucene_rs_list_2) + len(lucene_rs_list_3) + len(lucene_rs_list_4) + len(lucene_rs_list_5)
print("Total Issues: ", total_len)

prob1 = round(len(lucene_rs_list_1)/total_len, 2) * 100
prob2 = round(len(lucene_rs_list_2)/total_len, 2) * 100
prob3 = round(len(lucene_rs_list_3)/total_len, 2) * 100
prob4 = round(len(lucene_rs_list_4)/total_len, 2) * 100
prob5 = round(len(lucene_rs_list_5)/total_len, 2) * 100

random.shuffle(lucene_rs_list_1)
final_list_1 = lucene_rs_list_1[:prob1]
random.shuffle(lucene_rs_list_2)
final_list_2 = lucene_rs_list_2[:prob2]
random.shuffle(lucene_rs_list_3)
final_list_3 = lucene_rs_list_3[:prob3]
random.shuffle(lucene_rs_list_4)
final_list_4 = lucene_rs_list_4[:prob4]
random.shuffle(lucene_rs_list_5)
final_list_5 = lucene_rs_list_5[:prob5]

conn.close()

end_time = time()
time_taken = end_time - start_time

print("Total time taken in seconds: ", time_taken)
