from time import time
import re
import pymysql
import pymysql.cursors

start_time = time()

db = pymysql.connect(host='localhost', user='root', password='password', db='master_thesis', autocommit=True, use_unicode=True, charset="utf8")
cursor = db.cursor()

msg_list = list()
aut_list = list()
date_list = list()
com_list = list()
i = 0

with open('commit.txt') as f:
    for text in f:
        i+= 1
        if 'Author: ' in text:
            author = text.split("Author: ", 1)
            try:
                commit_author = author[1]
            except:
                commit_author = author[0]
            aut_list.append(commit_author)
        elif 'Date:   ' in text:
            date = text.split("Date:   ", 1)
            try:
                commit_date = date[1]
            except:
                commit_date = date[0]
            date_list.append(commit_date)
        elif text.startswith('commit '):
            commit = text.split("commit ", 1)
            commit_msg = 'https://github.com/apache/lucene-solr/tree/' + commit[0]
            com_list.append(commit_msg)
        else:
            if 'git-svn' in text:
                text = text
            elif text.startswith('Merge: '):
                text = text
            elif len(text.strip()) == 0:
                text = text
            elif len(text) == 5:
                text = text
            else:
                msg_list.append(text)

for x in range(len(msg_list)):
    try:
        cursor.execute("""INSERT INTO lucene_logs (commit_link, commit_msg, commit_author, commit_date) VALUES ("%s", "%s", "%s", "%s")""" % (com_list[x], msg_list[x], aut_list[x], date_list[x]))
        print("Inserted: ", msg_list[x])
    except:
        db.rollback()
        print("Failed to insert!")
