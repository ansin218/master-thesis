#!/usr/bin/env python

import xml.etree.ElementTree as ET
from time import time
import pymysql
import pymysql.cursors

db = pymysql.connect(host='localhost', user='root', password='password', db='master_thesis')
cursor = db.cursor()

start_time = time()
i = 1

for i in range(8):
    i = i + 1
    curxml = 'lucene_data_' + str(i) + '.xml'
    tree = ET.parse(curxml)
    root = tree.getroot()

    for channel in root.findall('channel'):
        for item in channel.iter('item'):
            title = item.find('title').text
            description = item.find('description').text
            assignee = item.find('assignee').text
            reporter = item.find('reporter').text
            for comment_author in item.iter('comment'):
                author = comment_author.get('author')
                comment = comment_author.text
                print("Parsing scraped data from ", curxml)
                print("Title: ", title)
                print("Description: ", description)
                print("Assignee: ", assignee)
                print("Reporter: ", reporter)
                print("Comment: ", comment)
                print("Author: ", author)

                refstr = "ViewProfile.jspa?name="
                if refstr in comment:
                    x = comment.split(refstr, 1)
                    x = x[1].split('"', 1)
                    tagged = x[0]
                    print("Tagged: ", tagged)
                else:
                    print("Tagged: None")

                try:
                    cursor.execute("""INSERT INTO lucene_try (title, description, comment, author, reporter, assignee, tagged) VALUES ("%s", "%s", "%s", "%s", "%s", "%s", "%s")""" % (title, description, comment, author, reporter, assignee, tagged))
                    db.commit()
                except:
                    db.rollback()

            print("\n")

db.close()
end_time = time()
time_taken = end_time - start_time

print("Total time taken in seconds: ", time_taken)
