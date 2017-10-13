#!/usr/bin/env python

import requests
from bs4 import BeautifulSoup
from time import time
import pymysql
import pymysql.cursors
import re

db = pymysql.connect(host='localhost', user='root', password='password', db='master_thesis', autocommit=True)
cursor = db.cursor()

start_time = time()

page = requests.get("https://bugzilla.mozilla.org/buglist.cgi?product=Thunderbird&component=Security&resolution=---")
soup = BeautifulSoup(page.content, 'html.parser')
i = 0
a_len = len(soup.find_all('a'))

for i in range(a_len):
    x = soup.find_all('a')[i].get_text()
    if(x.isnumeric()):
        link = "https://bugzilla.mozilla.org/show_bug.cgi?ctype=xml&id=" + x
        inner_page = requests.get(link)
        inner_soup = BeautifulSoup(inner_page.content, 'html.parser')
        ts_year = inner_soup.find_all('creation_ts')[0].get_text()
        ts_year = ts_year.split("-", 1)
        ts_year = ts_year[0]
        if(int(ts_year) >= 2012):
            title = inner_soup.find_all('short_desc')[0].get_text()
            print("Fetching: ", ts_year, title)
            reporter = inner_soup.find_all('reporter')[0].get_text()
            assignee = inner_soup.find_all('assigned_to')[0].get_text()
            description = inner_soup.find_all('thetext')[0].get_text()
            description = re.escape(description)
            comment_len = len(inner_soup.find_all('long_desc'))
            j = 0
            for j in range(comment_len):
                if(j >= 1):
                    author = inner_soup.find_all('who')[j].get_text()
                    comment = inner_soup.find_all('thetext')[j].get_text()
                    refstr = "comment #"
                    print("Parsing scraped data from ", link)
                    if refstr in comment:
                        try:
                            tagged = ""
                            x = comment.split(refstr, 1)
                            x = x[1].split(")", 1)
                            comment_id = x[0]
                            tagged = inner_soup.find_all('who')[int(comment_id)].get_text()
                        except ValueError:
                            tagged = "NULL"
                        except IndexError:
                            tagged = "NULL"
                    else:
                        tagged = "NULL"

                    try:
                        cursor.execute("""INSERT INTO thunderbird_try (title, description, comment, reporter, assignee, author, tagged) VALUES ("%s", "%s", "%s", "%s", "%s", "%s", "%s")""" % (title, description, comment, reporter, assignee, author, tagged))
                    except:
                        db.rollback()
        else:
            title = inner_soup.find_all('short_desc')[0].get_text()
            print("Skipping: ", ts_year, title)
        print("\n")

db.close()
end_time = time()
time_taken = end_time - start_time

print("Total time taken in seconds: ", time_taken)
