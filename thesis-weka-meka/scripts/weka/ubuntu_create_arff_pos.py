_author_ = 'Rana'

# generate arff file for working with weka

import arff
import pymysql


# connect to the database

db = pymysql.connect(host='localhost', user='root', password='password', db='Issue_Trackers')

cursor = db.cursor()


cursor.execute('SELECT sentence, isRelevant FROM b_ubuntu_pos_results')

messages = cursor.fetchall()


data = []


# make data vector for each tagged msg
for i, msg in enumerate(messages):
    if msg[1]==1:
        binary_class='relevant'
    else:
        binary_class = 'irrelevant'
    data.append([msg[0], binary_class])


arff.dump('Ubuntu_binary_pos.arff', data, relation="rationale", names=['sentence',  'classification'])


cursor.close()
db.close()

