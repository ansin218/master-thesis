import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.naive_bayes import MultinomialNB
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.linear_model import Perceptron
from sklearn.linear_model import SGDClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.pipeline import Pipeline
from sklearn.model_selection import KFold
from sklearn.metrics import confusion_matrix, f1_score

data = pd.read_csv("lucene_Ankur.csv")

texts = []
labels = []

for i, label in enumerate(data['isRelevant']):
    texts.append(data['sentence'][i])
    if label == 0:
        labels.append(0)
    else:
        labels.append(1)

texts = np.asarray(texts)
labels = np.asarray(labels)

print("Printing Label Ratio...")
print(np.bincount(labels))

######### NAIVE BAYES MODEL #########

nb_pipeline = Pipeline([
    ('vectorizer', CountVectorizer(ngram_range = (1, 10))),
    ('tfidf_transformer', TfidfTransformer()),
    ('classifier', MultinomialNB())
])

k_fold = KFold(n_splits = 10)
nb_scores = []
nb_conf_mat = np.array([[0, 0], [0, 0]])

for train_indices, test_indices in k_fold.split(data):

    train_text = data.iloc[train_indices]['sentence'].values
    train_y = data.iloc[train_indices]['isRelevant'].values

    test_text = data.iloc[test_indices]['sentence'].values
    test_y = data.iloc[test_indices]['isRelevant'].values

    nb_pipeline.fit(train_text, train_y)
    predictions = nb_pipeline.predict(test_text)

    nb_conf_mat += confusion_matrix(test_y, predictions)
    score = f1_score(test_y, predictions)
    nb_scores.append(score)

print("\nPrinting Results for Naive Bayes Model...")
print("Comments Classified: ", len(data))
print("Accuracy Score: ", sum(nb_scores)/len(nb_scores))
print("Confusion Matrix: ")
print(nb_conf_mat)

######### LOGISTIC REGRESSION MODEL #########

logit_pipeline = Pipeline([
    ('vectorizer', CountVectorizer(ngram_range = (1, 10))),
    ('tfidf_transformer', TfidfTransformer()),
    ('classifier', LogisticRegression())
])

logit_scores = []
logit_conf_mat = np.array([[0, 0], [0, 0]])

for train_indices, test_indices in k_fold.split(data):

    train_text = data.iloc[train_indices]['sentence'].values
    train_y = data.iloc[train_indices]['isRelevant'].values

    test_text = data.iloc[test_indices]['sentence'].values
    test_y = data.iloc[test_indices]['isRelevant'].values

    logit_pipeline.fit(train_text, train_y)
    predictions = logit_pipeline.predict(test_text)

    logit_conf_mat += confusion_matrix(test_y, predictions)
    score = f1_score(test_y, predictions)
    logit_scores.append(score)

print("\nPrinting Results for Logistic Regression Model...")
print("Comments Classified: ", len(data))
print("Accuracy Score: ", sum(logit_scores)/len(logit_scores))
print("Confusion Matrix: ")
print(logit_conf_mat)

######### SUPPORT VECTOR MACHINES MODEL #########

svc_pipeline = Pipeline([
    ('vectorizer', CountVectorizer(ngram_range = (1, 10))),
    ('tfidf_transformer', TfidfTransformer()),
    ('classifier', SVC())
])

svc_scores = []
svc_conf_mat = np.array([[0, 0], [0, 0]])

for train_indices, test_indices in k_fold.split(data):

    train_text = data.iloc[train_indices]['sentence'].values
    train_y = data.iloc[train_indices]['isRelevant'].values

    test_text = data.iloc[test_indices]['sentence'].values
    test_y = data.iloc[test_indices]['isRelevant'].values

    svc_pipeline.fit(train_text, train_y)
    predictions = svc_pipeline.predict(test_text)

    svc_conf_mat += confusion_matrix(test_y, predictions)
    score = f1_score(test_y, predictions)
    svc_scores.append(score)

print("\nPrinting Results for Support Vector Machines Model...")
print("Comments Classified: ", len(data))
print("Accuracy Score: ", sum(svc_scores)/len(svc_scores))
print("Confusion Matrix: ")
print(svc_conf_mat)

######### RANDOM FOREST MODEL #########

rf_pipeline = Pipeline([
    ('vectorizer', CountVectorizer(ngram_range = (1, 10))),
    ('tfidf_transformer', TfidfTransformer()),
    ('classifier', RandomForestClassifier())
])

rf_scores = []
rf_conf_mat = np.array([[0, 0], [0, 0]])

for train_indices, test_indices in k_fold.split(data):

    train_text = data.iloc[train_indices]['sentence'].values
    train_y = data.iloc[train_indices]['isRelevant'].values

    test_text = data.iloc[test_indices]['sentence'].values
    test_y = data.iloc[test_indices]['isRelevant'].values

    rf_pipeline.fit(train_text, train_y)
    predictions = rf_pipeline.predict(test_text)

    rf_conf_mat += confusion_matrix(test_y, predictions)
    score = f1_score(test_y, predictions)
    rf_scores.append(score)

print("\nPrinting Results for Random Forest Model...")
print("Comments Classified: ", len(data))
print("Accuracy Score: ", sum(rf_scores)/len(rf_scores))
print("Confusion Matrix: ")
print(rf_conf_mat)
