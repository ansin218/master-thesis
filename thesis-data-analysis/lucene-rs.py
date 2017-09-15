# -*- coding: utf-8 -*-
import pymysql
import pymysql.cursors
import random
from bs4 import BeautifulSoup
import nltk
from nltk import tokenize
from time import time

start_time = time()

conn = pymysql.connect(host='localhost', user='root', password='password', db='master_thesis', autocommit=True, use_unicode=True, charset="utf8")
cursor = conn.cursor()
cursor2 = conn.cursor()
cursor.execute("SELECT * FROM lucene_counter WHERE count > 5 AND count <= 30")

lucene_rs_list = list()

for row in cursor:
    lucene_rs_list.append(row[1])

random.shuffle(lucene_rs_list)
final_list = lucene_rs_list[:50]

for i in range(len(final_list)):
    print("PRINTING ISSUE NUMBER: ", i+1)
    current_title = final_list[i]
    query = "SELECT title, comment FROM lucene_try WHERE title = %s"
    cursor.execute(query, final_list[i])
    for row in cursor:
        root_comment = BeautifulSoup(row[1], "lxml").text
        print("Root Title: ", current_title)
        print("Root Comment: ", root_comment)
        cleancomment = tokenize.sent_tokenize(root_comment)
        for j in range(len(cleancomment)):
            print("Sub Comment: ", cleancomment[j])
            try:
                cursor2.execute("""INSERT INTO lucene_rs (title, root_comment, comment) VALUES ("%s", "%s", "%s")""" % (current_title, root_comment, cleancomment[j]))
            except:
                print()
        print("\n")

conn.close()

end_time = time()
time_taken = end_time - start_time

print("Total time taken in seconds: ", time_taken)
