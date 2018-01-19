import pandas as pd
import numpy as np
import scipy
import scipy.sparse as sp
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
from skmultilearn.problem_transform import BinaryRelevance, LabelPowerset, ClassifierChain
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import f1_score, accuracy_score, confusion_matrix
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics import classification_report
from sklearn.model_selection import KFold
from sklearn.pipeline import Pipeline

data = pd.read_csv("a_lucene_results.csv", dtype={'sentence':np.str_ })
#print(data.info())

y = data[['isIssue','isAlternative','isPro','isCon','isDecision']]
to_drop = ['id','isIssue','isAlternative','isPro','isCon','isDecision']
X = data.drop(to_drop, axis=1)

nb_pipeline = Pipeline([
    ('vectorizer', CountVectorizer()),
    ('classifier', BinaryRelevance(RandomForestClassifier()))
])

#count_vectorizer = CountVectorizer()
#counts = count_vectorizer.fit_transform(X['sentence'].values)

#X_train, X_test, y_train, y_test = train_test_split(counts, y, test_size=0.33)

kf = KFold(n_splits=10)


for train_index, test_index in kf.split(X, y):
    # assuming classifier object exists
    X_train = X[train_index,:]
    y_train = y[train_index,:]

    X_test = X[test_index,:]
    y_test = y[test_index,:]

    #clf = BinaryRelevance(RandomForestClassifier())
    #clf.fit(X_train, y_train)
    #y_pred = clf.predict(X_test)

    nb_pipline.fit(X_train, y_train)
    predictions = nb_pipline.predict(X_test)

    print(classification_report(y_test, y_pred))

#clf = BinaryRelevance(RandomForestClassifier())
#clf.fit(X_train, y_train)
#y_pred = clf.predict(X_test)

#print(classification_report(y_test, y_pred))
