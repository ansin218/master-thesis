#!/usr/bin/python

"""
str = "a href=\"https://issues.apache.org/jira/secure/ViewProfile.jspa?name=18519283579\"";
x = str.split('name=', 1 )
x = x[1].split('"', 1)
print(x[0])

str1 = "a href=\"https://issues.apache.org/jira/secure/ViewProfile.jspa?name=18519283579\"";
str2 = "ViewProfile.jspa?name=";

if(str2 in str1):
    print("Found")
else:
    print("Not Found")

print("str" + " " + "2")


for comments in root.iter('comments'):
    comment = comments.find('comment').text
    for comment_author in root.iter('comment'):
        author = comment_author.get('author')
        print(author)

"""

import pymysql
import pymysql.cursors

db = pymysql.connect(host='localhost', user='root', password='password', db='master_thesis')
cursor = db.cursor()

try:
    sql = "INSERT INTO lucene_try (title) VALUES (5)"
    cursor.execute(sql)
    db.commit()
finally:
    db.close()
