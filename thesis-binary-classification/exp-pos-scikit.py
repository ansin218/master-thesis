# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np
from time import time
import warnings
import string
import spacy
import en_core_web_sm

warnings.filterwarnings("ignore")

start_time = time()

data = pd.read_csv("a_lucene_results.csv")
print(data['sentence'])

nlp = en_core_web_sm.load()

sentenceList = data['sentence'].tolist()
posSentenceList = list()

for i in range(len(sentenceList)):
    doc = nlp(sentenceList[i])
    #print("Sentence ", i+1, ": ", sentenceList[i])
    outStr = ''
    for token in doc:
        combine = token.orth_ + "_" + token.tag_
        #print(combine)
        outStr = outStr + ' ' + combine
        #print("Word: ", token.orth_)
        #print("Upper Tag: ", token.pos_)
        #print("Lower Tag: ", token.tag_)
    #print(outStr)
    posSentenceList.append(outStr)

se = pd.Series(posSentenceList)
data['pos_tag'] = se.values

print(data['pos_tag'])

end_time = time()
time_taken = end_time - start_time

print("Total time taken in seconds: ", time_taken)
