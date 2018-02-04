_author_ = 'Ankur'

# generate arff file for working with Meka

import arff
import pymysql

# connect to the database

db = pymysql.connect(host='localhost', user='root', password='password', db='Issue_Trackers', autocommit=True, use_unicode=True, charset="utf8")
cursor = db.cursor()

cursor.execute('SELECT * FROM c_thunderbird_pos_results')
messages = cursor.fetchall()

data = []

# make data vector for each tagged msg
for i, msg in enumerate(messages):
    data.append([msg[5], msg[10], msg[11], msg[12], msg[13], msg[14]])

arff.dump('thunderbird_finegrained.arff', data, relation='rationale', names=['sentence','isIssue','isAlternative','isPro','isCon','isDecision'])

cursor.close()
db.close()
