#!/usr/bin/env python
import re
import pymysql
import pymysql.cursors

db = pymysql.connect(host='localhost', user='root', password='password', db='master_thesis', autocommit=True, use_unicode=True, charset="utf8")
cursor = db.cursor()

f = open('commit.txt','r')

author = ''
date = ''
msg_list = list()
aut_list = list()
date_list = list()
i = 0
while (i < 221295):
    i+=1
    text = f.readline()
    if 'Author' in text:
        author = author.split("Author: ", 1)
        try:
            print("Commit Author[1]: ", author[1])
            commit_author = author[1]
            aut_list.append(commit_author)
        except:
            print("Commit Author[0]: ", author[0])
            commit_author = author[0]
            aut_list.append(commit_author)
    if 'Date' in text:
        date = date.split("Date:   ", 1)
        try:
            print("Commit Date[1]: ", date[1])
            commit_date = date[1]
            date_list.append(commit_date)
        except:
            print("Commit Date[0]: ", date[0])
            commit_date = date[0]
            date_list.append(commit_date)
    if '    ' in text:
        if 'PR:' in text:
            text = text
        elif 'Obtained from:' in text:
            text = text
        elif  'Submitted by:' in text:
            text = text
        elif 'Reviewed by:' in text:
            text = text
        elif '    git-svn-id:' in text:
            text = text
        elif len(text) == 5:
            text = text
        else:
            commit_msg = text.replace("\n", "")
            msg_list.append(commit_msg)
