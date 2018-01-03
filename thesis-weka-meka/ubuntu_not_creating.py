_author_ = 'Ankur'

# generate arff file for working with Meka

import arff
import pymysql

# connect to the database

db = pymysql.connect(host='localhost', user='root', password='password', db='Issue_Trackers', autocommit=True, use_unicode=True, charset="utf8")
cursor = db.cursor()

cursor.execute('SELECT * FROM b_ubuntu_results')
messages = cursor.fetchall()

data = []

# make data vector for each tagged msg
for i, msg in enumerate(messages):
    data.append([msg[0], msg[1], msg[2], msg[3], msg[4], msg[5], msg[6], msg[7], msg[8], msg[9], msg[10], msg[11], msg[12], msg[13], msg[14]])

arff.dump('ubuntu_finegrained.arff', data, relation='rationale', names=['id','c_rss_id','comment_id','issue_id','comment','sentence','author','tagged','isRelevant','label','isIssue','isAlternative','isPro','isCon','isDecision'])

cursor.close()
db.close()
