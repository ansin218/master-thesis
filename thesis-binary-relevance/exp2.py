import pandas as pd
import numpy as np
import scipy
import scipy.sparse as sp
from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import train_test_split
from skmultilearn.problem_transform import BinaryRelevance, LabelPowerset, ClassifierChain
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import f1_score
from sklearn.feature_extraction.text import CountVectorizer

data = pd.read_csv("a_lucene_results.csv", dtype={'sentence':np.str_ })
print(data.info())

y = data[['isIssue','isAlternative','isPro','isCon','isDecision']]
to_drop = ['id','isIssue','isAlternative','isPro','isCon','isDecision']
X = data.drop(to_drop, axis=1)


count_vectorizer = CountVectorizer()
counts = count_vectorizer.fit_transform(X['sentence'].values)

X_train, X_test, y_train, y_test = train_test_split(counts, y, test_size=0.33)

clf = BinaryRelevance(RandomForestClassifier())

clf.fit(X_train, y_train)
y_pred = clf.predict(X_test)

print("The macro averaged F1-score is: %.3f" %(f1_score(y_pred, y_test, average='macro')))
