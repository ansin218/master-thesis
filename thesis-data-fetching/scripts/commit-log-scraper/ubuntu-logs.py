#!/usr/bin/env python

import requests
from bs4 import BeautifulSoup
from time import time
import re
import pymysql
import pymysql.cursors

start_time = time()

db = pymysql.connect(host='localhost', user='root', password='password', db='master_thesis', autocommit=True, use_unicode=True, charset="utf8")
cursor = db.cursor()

# Scrape commit logs from the following link and HTML structure
# HTML structure is subject to changes over time and may not work
# Changes need to be made to HTML tags accordingly 

for index_num in range(185000,  214051, 500):
    link = "https://code.launchpad.net/ubuntu/+code?field.lifecycle=DEVELOPMENT&field.lifecycle-empty-marker=1&field.sort_by=most+recently+changed+first&field.sort_by-empty-marker=1&memo=" + str(index_num) + "&start=" + str(index_num)
    page = requests.get(link)
    soup = BeautifulSoup(page.content, 'html.parser')
    a_len = len(soup.find_all('a'))

    for i in range(14, a_len, 1):
        x = soup.find_all('a')[i].get_text()
        try:
            latest_commit_id = soup.find_all('a')[i+1].get_text()
            str_hash = 'lp:'
            if str_hash in x:
                y = x.split(str_hash, 1)
                if(latest_commit_id.isnumeric()):
                    latest_commit_id = int(latest_commit_id)
                    for j in range(latest_commit_id):
                        branch_name = y[1].split('/', 1)
                        branch_name = branch_name[1].split('/', 1)
                        branch_name = '/' + branch_name[0]
                        link_2 = 'http://bazaar.launchpad.net/~ubuntu-branches/' + y[1] + branch_name + '/revision/' + str(j+1)
                        print(link_2)
                        try:
                            page_2 = requests.get(link_2)
                            soup_2 = BeautifulSoup(page_2.content, 'html.parser')
                            commit_author = soup_2.find_all('span')[2].get_text()
                            commit_date = soup_2.find_all('span')[3].get_text()
                            commit_msg = soup_2.find_all('div', class_='information')[0].get_text()
                            try:
                                commit_msg = re.escape(commit_msg)
                            except TypeError:
                                commit_msg = commit_msg
                            commit_link = link_2
                            print(link)
                            print(commit_link)
                            print("Commit Author: ", commit_author)
                            print("Commit Date: ", commit_date)
                            print("Commit Message: ", commit_msg)
                            print("\n")

                            try:
                                cursor.execute("""INSERT INTO ubuntu_logs (commit_link, commit_msg, commit_author, commit_date) VALUES ("%s", "%s", "%s", "%s")""" % (commit_link, commit_msg, commit_author, commit_date))
                            except:
                                db.rollback()
                        except:
                            print("Exception occurred, skipping")
        except IndexError:
            print("Index Error, Skipping")

end_time = time()
time_taken = end_time - start_time

print("Total time taken in seconds: ", time_taken)
