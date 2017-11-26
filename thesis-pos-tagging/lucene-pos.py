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
cursor_1.execute("SELECT * FROM lucene_rss_comments")

lucene_rss_list = list()
dump_list = list()

for row in cursor_1:
    lucene_rss_list.append(row[4])

#for x in range(len(lucene_rss_list)):
    #print(lucene_rss_list[x])

for i in range(len(lucene_rss_list)):
    doc = nlp(lucene_rss_list[i])
    print("Sentence ", i+1, ": ", lucene_rss_list[i])
    inner_dump_list = list()
    for token in doc:
        dump = json.dumps({ "word":token.orth_, "upper_tag":token.pos_, "lower_tag":token.tag_ })
        inner_dump_list.append(dump)
        print(dump)
    print(inner_dump_list)

end_time = time()
time_taken = end_time - start_time

print("Total time taken in seconds: ", time_taken)
