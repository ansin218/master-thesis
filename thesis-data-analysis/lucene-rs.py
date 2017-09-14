import pymysql
import pymysql.cursors
import random
from bs4 import BeautifulSoup
import nltk
from nltk import tokenize

conn = pymysql.connect(host='localhost', user='root', password='password', db='master_thesis', autocommit=True)
cursor = conn.cursor()
cursor.execute("SELECT * FROM lucene_counter WHERE count > 5 AND count <= 30")

lucene_rs_list = list()

for row in cursor:
    lucene_rs_list.append(row[1])

random.shuffle(lucene_rs_list)
final_list = lucene_rs_list[:1]

for i in range(len(final_list)):
    current_title = final_list[i]
    query = "SELECT title, comment FROM lucene_try WHERE title = %s"
    cursor.execute(query, final_list[i])
    for row in cursor:
        root_comment = BeautifulSoup(row[1], "lxml").text
        print("Root Title: ", current_title)
        sub_comment = tokenize.sent_tokenize(root_comment)
        print("Root Comment: ", root_comment)
        for j in range(len(sub_comment)):
            print("Sub Comment: ", sub_comment[j])
            #cursor.execute("""INSERT INTO lucene_rs (title, root_comment, comment) VALUES ("%s", "%s", "%s")""" % (current_title, root_comment, sub_comment[j]))
            #conn.commit()
        print("\n")
    print("\n")

conn.close()
