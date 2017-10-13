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

insert_cursor_1 = conn.cursor()
insert_cursor_2 = conn.cursor()
insert_cursor_3 = conn.cursor()
insert_cursor_4 = conn.cursor()
insert_cursor_5 = conn.cursor()

cursor_1 = conn.cursor()
cursor_1.execute("SELECT * FROM thunderbird_counter_rss WHERE count > 5 AND count <= 10")
cursor_2 = conn.cursor()
cursor_2.execute("SELECT * FROM thunderbird_counter_rss WHERE count > 10 AND count <= 15")
cursor_3 = conn.cursor()
cursor_3.execute("SELECT * FROM thunderbird_counter_rss WHERE count > 15 AND count <= 20")
cursor_4 = conn.cursor()
cursor_4.execute("SELECT * FROM thunderbird_counter_rss WHERE count > 20 AND count <= 25")
cursor_5 = conn.cursor()
cursor_5.execute("SELECT * FROM thunderbird_counter_rss WHERE count > 25 AND count <= 30")

thunderbird_rs_list_1 = list()
thunderbird_rs_list_2 = list()
thunderbird_rs_list_3 = list()
thunderbird_rs_list_4 = list()
thunderbird_rs_list_5 = list()

for row in cursor_1:
    thunderbird_rs_list_1.append(row[1])

for row in cursor_2:
    thunderbird_rs_list_2.append(row[1])

for row in cursor_3:
    thunderbird_rs_list_3.append(row[1])

for row in cursor_4:
    thunderbird_rs_list_4.append(row[1])

for row in cursor_5:
    thunderbird_rs_list_5.append(row[1])

total_len = len(thunderbird_rs_list_1) + len(thunderbird_rs_list_2) + len(thunderbird_rs_list_3) + len(thunderbird_rs_list_4) + len(thunderbird_rs_list_5)
print("Total Issues: ", total_len)

prob1 = int(round(len(thunderbird_rs_list_1)/total_len, 2) * 100)
prob2 = int(round(len(thunderbird_rs_list_2)/total_len, 2) * 100)
prob3 = int(round(len(thunderbird_rs_list_3)/total_len, 2) * 100)
prob4 = int(round(len(thunderbird_rs_list_4)/total_len, 2) * 100)
prob5 = int(round(len(thunderbird_rs_list_5)/total_len, 2) * 100)

random.shuffle(thunderbird_rs_list_1)
final_list_1 = thunderbird_rs_list_1[:prob1]
print("Number of issues between 5 and 10 comments: ", prob1)
for i in range(len(final_list_1)):
    print("PRINTING ISSUE NUMBER: ", i+1)
    current_title = final_list_1[i]
    query = "SELECT title, comment, id, description, author, reporter, assignee, tagged FROM thunderbird_try WHERE id >= 28237 AND title = %s"
    cursor_1.execute(query, final_list_1[i])
    for row in cursor_1:
        root_comment = BeautifulSoup(row[1], "lxml").text
        issue_id = row[2]
        author = row[4]
        reporter = row[5]
        assignee = row[6]
        tagged = row[7]
        current_title = current_title.strip()
        print("Root Title: ", current_title)
        cleancomment = tokenize.sent_tokenize(root_comment)
        for j in range(len(cleancomment)):
            try:
                insert_cursor_1.execute("""INSERT INTO thunderbird_rss (comment_id, title, root_comment, comment, author, reporter, assignee, tagged) VALUES ("%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s")""" % (issue_id, current_title, root_comment, cleancomment[j], author, reporter, assignee, tagged))
            except:
                print()
        print("\n")

random.shuffle(thunderbird_rs_list_2)
final_list_2 = thunderbird_rs_list_2[:prob2]
print("Number of issues between 10 and 15 comments: ", prob2)
for i in range(len(final_list_2)):
    print("PRINTING ISSUE NUMBER: ", i+1)
    current_title = final_list_2[i]
    query = "SELECT title, comment, id, description, author, reporter, assignee, tagged FROM thunderbird_try WHERE id >= 28237 AND title = %s"
    cursor_2.execute(query, final_list_2[i])
    for row in cursor_2:
        root_comment = BeautifulSoup(row[1], "lxml").text
        issue_id = row[2]
        author = row[4]
        reporter = row[5]
        assignee = row[6]
        tagged = row[7]
        current_title = current_title.strip()
        print("Root Title: ", current_title)
        cleancomment = tokenize.sent_tokenize(root_comment)
        for j in range(len(cleancomment)):
            try:
                insert_cursor_2.execute("""INSERT INTO thunderbird_rss (comment_id, title, root_comment, comment, author, reporter, assignee, tagged) VALUES ("%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s")""" % (issue_id, current_title, root_comment, cleancomment[j], author, reporter, assignee, tagged))
            except:
                print()
        print("\n")

random.shuffle(thunderbird_rs_list_3)
final_list_3 = thunderbird_rs_list_3[:prob3]
print("Number of issues between 15 and 20 comments: ", prob3)
for i in range(len(final_list_3)):
    print("PRINTING ISSUE NUMBER: ", i+1)
    current_title = final_list_3[i]
    query = "SELECT title, comment, id, description, author, reporter, assignee, tagged FROM thunderbird_try WHERE id >= 28237 AND title = %s"
    cursor_3.execute(query, final_list_3[i])
    for row in cursor_3:
        root_comment = BeautifulSoup(row[1], "lxml").text
        issue_id = row[2]
        author = row[4]
        reporter = row[5]
        assignee = row[6]
        tagged = row[7]
        current_title = current_title.strip()
        print("Root Title: ", current_title)
        cleancomment = tokenize.sent_tokenize(root_comment)
        for j in range(len(cleancomment)):
            try:
                insert_cursor_3.execute("""INSERT INTO thunderbird_rss (comment_id, title, root_comment, comment, author, reporter, assignee, tagged) VALUES ("%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s")""" % (issue_id, current_title, root_comment, cleancomment[j], author, reporter, assignee, tagged))
            except:
                print()
        print("\n")

random.shuffle(thunderbird_rs_list_4)
final_list_4 = thunderbird_rs_list_4[:prob4]
print("Number of issues between 20 and 25 comments: ", prob4)
for i in range(len(final_list_4)):
    print("PRINTING ISSUE NUMBER: ", i+1)
    current_title = final_list_4[i]
    query = "SELECT title, comment, id, description, author, reporter, assignee, tagged FROM thunderbird_try WHERE id >= 28237 AND title = %s"
    cursor_4.execute(query, final_list_4[i])
    for row in cursor_4:
        root_comment = BeautifulSoup(row[1], "lxml").text
        issue_id = row[2]
        author = row[4]
        reporter = row[5]
        assignee = row[6]
        tagged = row[7]
        current_title = current_title.strip()
        print("Root Title: ", current_title)
        cleancomment = tokenize.sent_tokenize(root_comment)
        for j in range(len(cleancomment)):
            try:
                insert_cursor_4.execute("""INSERT INTO thunderbird_rss (comment_id, title, root_comment, comment, author, reporter, assignee, tagged) VALUES ("%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s")""" % (issue_id, current_title, root_comment, cleancomment[j], author, reporter, assignee, tagged))
            except:
                print()
        print("\n")

random.shuffle(thunderbird_rs_list_5)
final_list_5 = thunderbird_rs_list_5[:prob5]
print("Number of issues between 25 and 30 comments: ", prob5)
for i in range(len(final_list_5)):
    print("PRINTING ISSUE NUMBER: ", i+1)
    current_title = final_list_5[i]
    query = "SELECT title, comment, id, description, author, reporter, assignee, tagged FROM thunderbird_try WHERE id >= 28237 AND title = %s"
    cursor_5.execute(query, final_list_5[i])
    for row in cursor_5:
        root_comment = BeautifulSoup(row[1], "lxml").text
        issue_id = row[2]
        author = row[4]
        reporter = row[5]
        assignee = row[6]
        tagged = row[7]
        current_title = current_title.strip()
        print("Root Title: ", current_title)
        cleancomment = tokenize.sent_tokenize(root_comment)
        for j in range(len(cleancomment)):
            try:
                insert_cursor_5.execute("""INSERT INTO thunderbird_rss (comment_id, title, root_comment, comment, author, reporter, assignee, tagged) VALUES ("%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s")""" % (issue_id, current_title, root_comment, cleancomment[j], author, reporter, assignee, tagged))
            except:
                print()
        print("\n")

conn.close()

end_time = time()
time_taken = end_time - start_time

print("Total time taken in seconds: ", time_taken)
