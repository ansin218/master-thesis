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

conn = pymysql.connect(host='localhost', user='root', password='password', db='Issue_Trackers', autocommit=True, use_unicode=True, charset="utf8")

insert_cursor_1 = conn.cursor()
insert_cursor_2 = conn.cursor()
insert_cursor_3 = conn.cursor()
insert_cursor_4 = conn.cursor()
insert_cursor_5 = conn.cursor()
insert_cursor_6 = conn.cursor()
insert_cursor_7 = conn.cursor()
insert_cursor_8 = conn.cursor()
insert_cursor_9 = conn.cursor()
insert_cursor_10 = conn.cursor()

# Load dataset based on issue number
# These numbers correspond to relevant time frame

cursor_1 = conn.cursor()
cursor_1.execute("SELECT * FROM thunderbird_issues_new WHERE comments_count > 5 AND comments_count <= 10")
cursor_2 = conn.cursor()
cursor_2.execute("SELECT * FROM thunderbird_issues_new WHERE comments_count > 10 AND comments_count <= 15")
cursor_3 = conn.cursor()
cursor_3.execute("SELECT * FROM thunderbird_issues_new WHERE comments_count > 15 AND comments_count <= 20")
cursor_4 = conn.cursor()
cursor_4.execute("SELECT * FROM thunderbird_issues_new WHERE comments_count > 20 AND comments_count <= 25")
cursor_5 = conn.cursor()
cursor_5.execute("SELECT * FROM thunderbird_issues_new WHERE comments_count > 25 AND comments_count <= 30")

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

# Stratified Sampling Based on Ratios
random.shuffle(thunderbird_rs_list_1)
final_list_1 = thunderbird_rs_list_1[:prob1]
print("Number of issues between 5 and 10 comments: ", prob1)
for i in range(len(final_list_1)):
    print("PRINTING ISSUE NUMBER: ", i+1)
    current_title = final_list_1[i]
    query = "SELECT * FROM thunderbird_issues_new, thunderbird_comments_new WHERE thunderbird_issues_new.issue_id = thunderbird_comments_new.issue_id AND title = %s"
    cursor_1.execute(query, final_list_1[i])
    for row in cursor_1:
        root_comment = BeautifulSoup(row[8], "lxml").text
        issue_id = row[7]
        comment_id = row[6]
        author = row[9]
        reporter = row[3]
        assignee = row[4]
        tagged = row[10]
        current_title = current_title.strip()
        print("Root Title: ", current_title)
        cleancomment = tokenize.sent_tokenize(root_comment)
        try:
            insert_cursor_1.execute("""INSERT INTO thunderbird_rss_issues (issue_id, title, reporter, assignee) VALUES ("%s", "%s", "%s", "%s")""" % (issue_id, current_title, reporter, assignee))
        except:
            print("")
        for j in range(len(cleancomment)):
            try:
                insert_cursor_6.execute("""INSERT INTO thunderbird_rss_comments (comment_id, issue_id, comment, sentence, author, tagged) VALUES ("%s", "%s", "%s", "%s", "%s", "%s")""" % (comment_id, issue_id, root_comment, cleancomment[j], author, tagged))
            except:
                print("")
        print("\n")

random.shuffle(thunderbird_rs_list_2)
final_list_2 = thunderbird_rs_list_2[:prob2]
print("Number of issues between 10 and 15 comments: ", prob2)
for i in range(len(final_list_2)):
    print("PRINTING ISSUE NUMBER: ", i+1)
    current_title = final_list_2[i]
    query = "SELECT * FROM thunderbird_issues_new, thunderbird_comments_new WHERE thunderbird_issues_new.issue_id = thunderbird_comments_new.issue_id AND title = %s"
    cursor_2.execute(query, final_list_2[i])
    for row in cursor_2:
        root_comment = BeautifulSoup(row[8], "lxml").text
        issue_id = row[7]
        comment_id = row[6]
        author = row[9]
        reporter = row[3]
        assignee = row[4]
        tagged = row[10]
        print("Root Title: ", current_title)
        cleancomment = tokenize.sent_tokenize(root_comment)
        try:
            insert_cursor_2.execute("""INSERT INTO thunderbird_rss_issues (issue_id, title, reporter, assignee) VALUES ("%s", "%s", "%s", "%s")""" % (issue_id, current_title, reporter, assignee))
        except:
            print("")
        for j in range(len(cleancomment)):
            try:
                insert_cursor_7.execute("""INSERT INTO thunderbird_rss_comments (comment_id, issue_id, comment, sentence, author, tagged) VALUES ("%s", "%s", "%s", "%s", "%s", "%s")""" % (comment_id, issue_id, root_comment, cleancomment[j], author, tagged))
            except:
                print("")
        print("\n")

random.shuffle(thunderbird_rs_list_3)
final_list_3 = thunderbird_rs_list_3[:prob3]
print("Number of issues between 15 and 20 comments: ", prob3)
for i in range(len(final_list_3)):
    print("PRINTING ISSUE NUMBER: ", i+1)
    current_title = final_list_3[i]
    query = "SELECT * FROM thunderbird_issues_new, thunderbird_comments_new WHERE thunderbird_issues_new.issue_id = thunderbird_comments_new.issue_id AND title = %s"
    cursor_3.execute(query, final_list_3[i])
    for row in cursor_3:
        root_comment = BeautifulSoup(row[8], "lxml").text
        issue_id = row[7]
        comment_id = row[6]
        author = row[9]
        reporter = row[3]
        assignee = row[4]
        tagged = row[10]
        current_title = current_title.strip()
        print("Root Title: ", current_title)
        cleancomment = tokenize.sent_tokenize(root_comment)
        try:
            insert_cursor_3.execute("""INSERT INTO thunderbird_rss_issues (issue_id, title, reporter, assignee) VALUES ("%s", "%s", "%s", "%s")""" % (issue_id, current_title, reporter, assignee))
        except:
            print("")
        for j in range(len(cleancomment)):
            try:
                insert_cursor_8.execute("""INSERT INTO thunderbird_rss_comments (comment_id, issue_id, comment, sentence, author, tagged) VALUES ("%s", "%s", "%s", "%s", "%s", "%s")""" % (comment_id, issue_id, root_comment, cleancomment[j], author, tagged))
            except:
                print("")
        print("\n")

random.shuffle(thunderbird_rs_list_4)
final_list_4 = thunderbird_rs_list_4[:prob4]
print("Number of issues between 20 and 25 comments: ", prob4)
for i in range(len(final_list_4)):
    print("PRINTING ISSUE NUMBER: ", i+1)
    current_title = final_list_4[i]
    query = "SELECT * FROM thunderbird_issues_new, thunderbird_comments_new WHERE thunderbird_issues_new.issue_id = thunderbird_comments_new.issue_id AND title = %s"
    cursor_4.execute(query, final_list_4[i])
    for row in cursor_4:
        root_comment = BeautifulSoup(row[8], "lxml").text
        issue_id = row[7]
        comment_id = row[6]
        author = row[9]
        reporter = row[3]
        assignee = row[4]
        tagged = row[10]
        current_title = current_title.strip()
        print("Root Title: ", current_title)
        cleancomment = tokenize.sent_tokenize(root_comment)
        try:
            insert_cursor_4.execute("""INSERT INTO thunderbird_rss_issues (issue_id, title, reporter, assignee) VALUES ("%s", "%s", "%s", "%s")""" % (issue_id, current_title, reporter, assignee))
        except:
            print("")
        for j in range(len(cleancomment)):
            try:
                insert_cursor_9.execute("""INSERT INTO thunderbird_rss_comments (comment_id, issue_id, comment, sentence, author, tagged) VALUES ("%s", "%s", "%s", "%s", "%s", "%s")""" % (comment_id, issue_id, root_comment, cleancomment[j], author, tagged))
            except:
                print("")
        print("\n")

random.shuffle(thunderbird_rs_list_5)
final_list_5 = thunderbird_rs_list_5[:prob5]
print("Number of issues between 25 and 30 comments: ", prob5)
for i in range(len(final_list_5)):
    print("PRINTING ISSUE NUMBER: ", i+1)
    current_title = final_list_5[i]
    query = "SELECT * FROM thunderbird_issues_new, thunderbird_comments_new WHERE thunderbird_issues_new.issue_id = thunderbird_comments_new.issue_id AND title = %s"
    cursor_5.execute(query, final_list_5[i])
    for row in cursor_5:
        root_comment = BeautifulSoup(row[8], "lxml").text
        issue_id = row[7]
        comment_id = row[6]
        author = row[9]
        reporter = row[3]
        assignee = row[4]
        tagged = row[10]
        current_title = current_title.strip()
        print("Root Title: ", current_title)
        cleancomment = tokenize.sent_tokenize(root_comment)
        try:
            insert_cursor_5.execute("""INSERT INTO thunderbird_rss_issues (issue_id, title, reporter, assignee) VALUES ("%s", "%s", "%s", "%s")""" % (issue_id, current_title, reporter, assignee))
        except:
            print("")
        for j in range(len(cleancomment)):
            try:
                insert_cursor_10.execute("""INSERT INTO thunderbird_rss_comments (comment_id, issue_id, comment, sentence, author, tagged) VALUES ("%s", "%s", "%s", "%s", "%s", "%s")""" % (comment_id, issue_id, root_comment, cleancomment[j], author, tagged))
            except:
                print("")
        print("\n")

conn.close()

end_time = time()
time_taken = end_time - start_time

print("Total time taken in seconds: ", time_taken)
