# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np
from time import time
import warnings
import string
import spacy
import en_core_web_sm
import pymysql
import pymysql.cursors

db = pymysql.connect(host='localhost', user='root', password='password', db='Issue_Trackers', autocommit=True, use_unicode=True, charset="utf8")
cursor = db.cursor()

warnings.filterwarnings("ignore")

start_time = time()

data = pd.read_csv("b_ubuntu_results.csv")

nlp = en_core_web_sm.load()

crssIdList = data['c_rss_id'].tolist()
commentIdList = data['comment_id'].tolist()
issueIdList = data['issue_id'].tolist()
commentList = data['comment'].tolist()
authorList = data['author'].tolist()
isRelevantList = data['isRelevant'].tolist()
labelList = data['label'].tolist()
isIssueList = data['isIssue'].tolist()
isAlternativeList = data['isAlternative'].tolist()
isProList = data['isPro'].tolist()
isConList = data['isCon'].tolist()
isDecisionList = data['isDecision'].tolist()
taggedList = data['tagged'].tolist()
sentenceList = data['sentence'].tolist()
posSentenceList = list()

for i in range(len(sentenceList)):
    doc = nlp(sentenceList[i])
    outStr = ''
    for token in doc:
        combine = token.orth_ + "_" + token.tag_
        outStr = outStr + ' ' + combine
    posSentenceList.append(outStr)

se = pd.Series(posSentenceList)
data['pos_tag'] = se.values

for i in range(len(crssIdList)):
	try:
		cursor.execute("""INSERT INTO b_ubuntu_pos_results (c_rss_id, comment_id, issue_id, comment, sentence, author, tagged, isRelevant, label, isIssue, isAlternative, isPro, isCon, isDecision) VALUES ("%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s")""" % (crssIdList[i], commentIdList[i], issueIdList[i], commentList[i], posSentenceList[i], authorList[i], taggedList[i], isRelevantList[i], labelList[i], isIssueList[i], isAlternativeList[i], isProList[i], isConList[i], isDecisionList[i]))
		print('Inserting record ', i+1)
	except:
		db.rollback()

end_time = time()
time_taken = end_time - start_time

print("Total time taken in seconds: ", time_taken)