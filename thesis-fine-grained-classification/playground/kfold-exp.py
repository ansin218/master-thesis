import pandas as pd
import numpy as np
import scipy
import scipy.sparse as sp
from sklearn.model_selection import train_test_split
from skmultilearn.problem_transform import BinaryRelevance
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics import classification_report
from sklearn.cross_validation import cross_val_predict

data = pd.read_csv("a_lucene_results.csv", dtype={'sentence':np.str_ })
#print(data.info())

y = data[['isIssue','isAlternative','isPro','isCon','isDecision']]
to_drop = ['id','isIssue','isAlternative','isPro','isCon','isDecision']
X = data.drop(to_drop, axis=1)

count_vectorizer = CountVectorizer()
counts = count_vectorizer.fit_transform(X['sentence'].values)

#X_train, X_test, y_train, y_test = train_test_split(counts, y, test_size=0.33)

clf = BinaryRelevance(RandomForestClassifier())

y_pred = cross_val_predict(clf, counts, y, cv=10)

print(classification_report(y, y_pred))

#clf.fit(X_train, y_train)
#y_pred = clf.predict(X_test)

# Print invidiual label wise F1, precision and recall scores
#target_names = ['A', 'B', 'C', 'D', 'E']
#print(classification_report(y_pred, y_test))

# Extract the values of label A alone, repeat the same for other labels
#extractedData1 = y_pred[:,[1]]
#z = scipy.sparse.csr_matrix(y_test)
#extractedData2 = z[:,[1]]

# Flatten both the array and print the accuracy score for label A
#actual = extractedData1.toarray().flatten()
#predicted = extractedData2.toarray().flatten()
#print(accuracy_score(actual, predicted))