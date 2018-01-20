import pandas as pd
import numpy as np
import scipy
import scipy.sparse as sp
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.stop_words import ENGLISH_STOP_WORDS as stopwords
from skmultilearn.problem_transform import BinaryRelevance
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import MultinomialNB
from sklearn.svm import LinearSVC
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics import classification_report
from sklearn.cross_validation import cross_val_predict
from time import time
import warnings

warnings.filterwarnings("ignore")

start_time = time()

data = pd.read_csv("a_lucene_results.csv", dtype={'sentence':np.str_ })

y = data[['isIssue','isAlternative','isPro','isCon','isDecision']]
to_drop = ['id','isIssue','isAlternative','isPro','isCon','isDecision']
X = data.drop(to_drop, axis=1)
target_names = ['isIssue','isAlternative','isPro','isCon','isDecision']

count_vectorizer = CountVectorizer()
counts = count_vectorizer.fit_transform(X['sentence'].values)
transformer = TfidfTransformer()
counts = transformer.fit_transform(counts)

# LOGISTIC REGRESSION MODEL
clf = BinaryRelevance(LogisticRegression())
y_pred = cross_val_predict(clf, counts, y, cv=10)
print("\nClassification Report for Logistic Regression\n")
print(classification_report(y, y_pred, target_names=target_names))

# MULTINOMIAL NAIVE BAYES MODEL
clf = BinaryRelevance(MultinomialNB())
y_pred = cross_val_predict(clf, counts, y, cv=10)
print("\nClassification Report for Multinomial Naive Bayes\n")
print(classification_report(y, y_pred, target_names=target_names))

# SUPPORT VECTOR MACHINE MODEL
clf = BinaryRelevance(LinearSVC())
y_pred = cross_val_predict(clf, counts, y, cv=10)
print("\nClassification Report for Support Vector Machine\n")
print(classification_report(y, y_pred, target_names=target_names))

# DECISION TREE MODEL
clf = BinaryRelevance(DecisionTreeClassifier())
y_pred = cross_val_predict(clf, counts, y, cv=10)
print("\nClassification Report for Decision Tree\n")
print(classification_report(y, y_pred, target_names=target_names))

# RANDOM FOREST MODEL
clf = BinaryRelevance(RandomForestClassifier())
y_pred = cross_val_predict(clf, counts, y, cv=10)
print("\nClassification Report for Random Forest\n")
print(classification_report(y, y_pred, target_names=target_names))

end_time = time()
time_taken = end_time - start_time

print("Total time taken in seconds: ", time_taken)