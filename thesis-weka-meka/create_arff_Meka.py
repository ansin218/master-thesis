_author_ = 'Rana'

# generate arff file for working with Meka

import arff
import pymysql


# connect to the database

db = pymysql.connect(host='localhost', user='', password='', db='IRC_Main_Study')

cursor = db.cursor()


cursor.execute('SELECT index_id,message, isIssue,isAlternative,isPro,isCon,isDecision FROM message_fine_grained')

messages = cursor.fetchall()


data = []

# make data vector for each tagged msg
for i, msg in enumerate(messages):
    data.append([msg[0], msg[1], msg[2], msg[3], msg[4], msg[5],msg[6]])


arff.dump('message_finegrained.arff', data, relation="rationale", names=['id','message',  'isIssue', 'isAlternative', 'isPro', 'isCon', 'isDecision'])


cursor.close()
db.close()


