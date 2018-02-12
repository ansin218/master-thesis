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

# Put commit.txt in same directory as this file
# Parse commit.txt file to get necessary data
# This file does not scrape but only parses downloaded logs data

with open('commit.txt') as f:
    for text in f:
        if text.startswith('changeset:   '):
            commit = text.split("changeset:   ", 1)
            commit_id = commit[1].split(":", 1)
            commit_link = 'https://hg.mozilla.org/comm-central/rev/' + commit_id[1]
            com_list.append(commit_link)
        elif text.startswith('user:        '):
            committer = text.split("user:        ", 1)
            aut_list.append(committer[1])
        elif text.startswith('date:        '):
            date = text.split("date:        ", 1)
            date_list.append(date[1])
        elif text.startswith('summary:     '):
            msg = text.split("summary:     ", 1)
            msg_list.append(msg[1])


for x in range(len(msg_list)):
    try:
        cursor.execute("""INSERT INTO thunderbird_logs (commit_link, commit_msg, commit_author, commit_date) VALUES ("%s", "%s", "%s", "%s")""" % (com_list[x], msg_list[x], aut_list[x], date_list[x]))
        print("Inserted: ", msg_list[x])
    except:
        db.rollback()
        print("Failed to insert!")


end_time = time()
time_taken = end_time - start_time

print("Total time taken in seconds: ", time_taken)
