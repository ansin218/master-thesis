_author_ = 'Rana'

# generate arff file for working with weka

import arff
import pymysql


# connect to the database

db = pymysql.connect(host='localhost', user='', password='', db='Issues_Main')

cursor = db.cursor()


cursor.execute('SELECT id,sentence,isRelevant FROM a_lucene_results')

messages = cursor.fetchall()


data = []


# make data vector for each tagged msg
for i, msg in enumerate(messages):
    if msg[2]==1:
        binary_class='relevant'
    else:
        binary_class = 'irrelevant'
    data.append([msg[0], msg[1], binary_class])


arff.dump('Lucene_binary.arff', data, relation="rationale", names=['id','sentence',  'classification'])


cursor.close()
db.close()


