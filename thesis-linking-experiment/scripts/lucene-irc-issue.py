# -*- coding: utf-8 -*-
import pymysql
import pymysql.cursors
from fuzzywuzzy import fuzz
from fuzzywuzzy import process
from time import time

start_time = time()

conn = pymysql.connect(host='localhost', user='root', password='password', db='Issue_Trackers', autocommit=True, use_unicode=True, charset="utf8")

# Load keywords of issues and IRCs
cursor_1 = conn.cursor()
cursor_1.execute("SELECT issue_id, comment_id, keywords FROM lucene_issues_keywords_lda")

cursor_2 = conn.cursor()
cursor_2.execute("SELECT msg_id, keywords FROM lucene_irc_keywords_lda")

cursor_3 = conn.cursor()

issue_keyword_list = list()
issue_id_list = list()
comment_id_list = list()
irc_keyword_list = list()
irc_id_list = list()


for row in cursor_1:
	issue_id_list.append(row[0])
	comment_id_list.append(row[1])
	issue_keyword_list.append(row[2])

for row in cursor_2:
	irc_id_list.append(row[0])
	irc_keyword_list.append(row[1])

# Perform similarity between keywords using string matching Levenshtein distance
for x in range(len(issue_keyword_list)):
	if(issue_keyword_list[x] != 'Insufficient Data'):
		for y in range(len(irc_keyword_list)):
			if(irc_keyword_list[y] != 'Insufficient Data'):
				z = fuzz.token_sort_ratio(issue_keyword_list[x], irc_keyword_list[y])
				if(z > 50):
					print('Issue ID and ', issue_id_list[x], ' Comment ID ', comment_id_list[x], ' is similar to ', irc_id_list[y], ' by ', z, '%')
					print('\n')
					try:
					    cursor_3.execute("""INSERT INTO lucene_issue_irc (issue_id, comment_id, irc_msg_id, similarity) VALUES ("%s", "%s", "%s", "%s")""" % (issue_id_list[x], comment_id_list[x], irc_id_list[y], z))
					except:
					    conn.rollback()

end_time = time()
time_taken = end_time - start_time

print("Total time taken in seconds: ", time_taken)
