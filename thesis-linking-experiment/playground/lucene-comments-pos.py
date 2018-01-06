# -*- coding: utf-8 -*-
import pymysql
import pymysql.cursors
from time import time
import spacy
import en_core_web_sm
import json

start_time = time()

nlp = en_core_web_sm.load()

conn = pymysql.connect(host='localhost', user='root', password='password', db='Issue_Trackers', autocommit=True, use_unicode=True, charset="utf8")

cursor_1 = conn.cursor()
cursor_1.execute("SELECT DISTINCT(comment), comment_id, issue_id FROM `lucene_rss_comments` WHERE 1")

lucene_rss_list = list()
dump_list = list()

for row in cursor_1:
    lucene_rss_list.append(row[0])

for i in range(len(lucene_rss_list)):
    doc = nlp(lucene_rss_list[i])
    print("Comment ", i+1)
    inner_dump_list = list()
    for token in doc:
    	if(token.pos_ == 'NOUN'):
        	print(token.orth_, token.pos_, token.tag_)
    print('\n')

end_time = time()
time_taken = end_time - start_time

print("Total time taken in seconds: ", time_taken)