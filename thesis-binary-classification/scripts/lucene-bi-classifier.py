# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np
from time import time
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import MultinomialNB
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.stop_words import ENGLISH_STOP_WORDS as stopwords
from sklearn.pipeline import Pipeline
from sklearn.model_selection import KFold
from sklearn.base import TransformerMixin
from sklearn.metrics import confusion_matrix, accuracy_score, f1_score, precision_score, recall_score
from imblearn.over_sampling import SMOTE
from imblearn.under_sampling import RandomUnderSampler
import warnings
import string
import spacy
import en_core_web_sm

warnings.filterwarnings("ignore")

start_time = time()

data = pd.read_csv("a_lucene_results.csv")

nlp = en_core_web_sm.load()

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

punctuations = string.punctuation

parser = en_core_web_sm.load()

# Custom transformer using spaCy
class predictors(TransformerMixin):
    def transform(self, X, **transform_params):
        return [clean_text(text) for text in X]
    def fit(self, X, y=None, **fit_params):
        return self
    def get_params(self, deep=True):
        return {}

# Basic utility function to clean the text
def clean_text(text):
    return text.strip().lower()

def spacy_tokenizer(sentence):
    tokens = parser(sentence)
    tokens = [tok.lemma_.lower().strip() if tok.lemma_ != "-PRON-" else tok.lower_ for tok in tokens]
    tokens = [tok for tok in tokens if (tok not in stopwords and tok not in punctuations)]
    return tokens

data['isRelevant'] = data['isRelevant'].map({0: 1, 1: 0})

######### LOGISTIC REGRESSION MODEL #########

logit_pipeline = Pipeline([
    ('vectorizer', CountVectorizer(ngram_range = (1, 3))),
    ('tfidf_transformer', TfidfTransformer()),
    ('classifier', LogisticRegression())
])

k_fold = KFold(n_splits = 10)
logit_f1_scores = []
logit_ac_scores = []
logit_pr_scores = []
logit_re_scores = []
logit_conf_mat = np.array([[0, 0], [0, 0]])

for train_indices, test_indices in k_fold.split(data):
    try:
        train_text = data.iloc[train_indices]['pos_tag'].values
        train_y = data.iloc[train_indices]['isRelevant'].values

        test_text = data.iloc[test_indices]['pos_tag'].values
        test_y = data.iloc[test_indices]['isRelevant'].values

        logit_pipeline.fit(train_text, train_y)
        predictions = logit_pipeline.predict(test_text)

        logit_conf_mat += confusion_matrix(test_y, predictions)
        score1 = f1_score(test_y, predictions)
        logit_f1_scores.append(score1)
        score2 = accuracy_score(test_y, predictions)
        logit_ac_scores.append(score2)
        score3 = precision_score(test_y, predictions)
        logit_pr_scores.append(score3)
        score4 = recall_score(test_y, predictions)
        logit_re_scores.append(score4)
    except:
        print("Skipping Corrupt Lines")

print("\nPrinting Results for Logistic Regression Model...")
print("Comments Classified: ", len(data))
print("F1 Score: ", sum(logit_f1_scores)/len(logit_f1_scores))
print("Accuracy Score: ", sum(logit_ac_scores)/len(logit_ac_scores))
print("Precision Score: ", sum(logit_pr_scores)/len(logit_pr_scores))
print("Recall Score: ", sum(logit_re_scores)/len(logit_re_scores))
print("Confusion Matrix: ")
print(logit_conf_mat)

######### NAIVE BAYES MODEL #########

nb_pipeline = Pipeline([
    ('vectorizer', CountVectorizer(ngram_range = (1, 3))),
    ('tfidf_transformer', TfidfTransformer()),
    ('classifier', MultinomialNB())
])

k_fold = KFold(n_splits = 10)
nb_f1_scores = []
nb_ac_scores = []
nb_pr_scores = []
nb_re_scores = []
nb_conf_mat = np.array([[0, 0], [0, 0]])

for train_indices, test_indices in k_fold.split(data):

    train_text = data.iloc[train_indices]['pos_tag'].values
    train_y = data.iloc[train_indices]['isRelevant'].values

    test_text = data.iloc[test_indices]['pos_tag'].values
    test_y = data.iloc[test_indices]['isRelevant'].values

    nb_pipeline.fit(train_text, train_y)
    predictions = nb_pipeline.predict(test_text)

    nb_conf_mat += confusion_matrix(test_y, predictions)
    score1 = f1_score(test_y, predictions)
    nb_f1_scores.append(score1)
    score2 = accuracy_score(test_y, predictions)
    nb_ac_scores.append(score2)
    score3 = precision_score(test_y, predictions)
    nb_pr_scores.append(score3)
    score4 = recall_score(test_y, predictions)
    nb_re_scores.append(score4)

print("\nPrinting Results for Naive Bayes Model...")
print("Comments Classified: ", len(data))
print("F1 Score: ", sum(nb_f1_scores)/len(nb_f1_scores))
print("Accuracy Score: ", sum(nb_ac_scores)/len(nb_ac_scores))
print("Precision Score: ", sum(nb_pr_scores)/len(nb_pr_scores))
print("Recall Score: ", sum(nb_re_scores)/len(nb_re_scores))
print("Confusion Matrix: ")
print(nb_conf_mat)

######### SUPPORT VECTOR MACHINES MODEL #########

svc_pipeline = Pipeline([
    ('vectorizer', CountVectorizer(ngram_range = (1, 3))),
    ('tfidf_transformer', TfidfTransformer()),
    ('classifier', SVC())
])

k_fold = KFold(n_splits = 10)
svc_f1_scores = []
svc_ac_scores = []
svc_pr_scores = []
svc_re_scores = []
svc_conf_mat = np.array([[0, 0], [0, 0]])

for train_indices, test_indices in k_fold.split(data):

    train_text = data.iloc[train_indices]['pos_tag'].values
    train_y = data.iloc[train_indices]['isRelevant'].values

    test_text = data.iloc[test_indices]['pos_tag'].values
    test_y = data.iloc[test_indices]['isRelevant'].values

    svc_pipeline.fit(train_text, train_y)
    predictions = svc_pipeline.predict(test_text)

    svc_conf_mat += confusion_matrix(test_y, predictions)
    score1 = f1_score(test_y, predictions)
    svc_f1_scores.append(score1)
    score2 = accuracy_score(test_y, predictions)
    svc_ac_scores.append(score2)
    score3 = precision_score(test_y, predictions)
    svc_pr_scores.append(score3)
    score4 = recall_score(test_y, predictions)
    svc_re_scores.append(score4)

print("\nPrinting Results for Support Vector Machines Model...")
print("Comments Classified: ", len(data))
print("F1 Score: ", sum(svc_f1_scores)/len(svc_f1_scores))
print("Accuracy Score: ", sum(svc_ac_scores)/len(svc_ac_scores))
print("Precision Score: ", sum(svc_pr_scores)/len(svc_pr_scores))
print("Recall Score: ", sum(svc_re_scores)/len(svc_re_scores))
print("Confusion Matrix: ")
print(svc_conf_mat)

######### RANDOM FOREST MODEL #########

rf_pipeline = Pipeline([
    ('vectorizer', CountVectorizer(ngram_range = (1, 3))),
    ('tfidf_transformer', TfidfTransformer()),
    ('classifier', RandomForestClassifier())
])

k_fold = KFold(n_splits = 10)
rf_f1_scores = []
rf_ac_scores = []
rf_pr_scores = []
rf_re_scores = []
rf_conf_mat = np.array([[0, 0], [0, 0]])

for train_indices, test_indices in k_fold.split(data):

    train_text = data.iloc[train_indices]['pos_tag'].values
    train_y = data.iloc[train_indices]['isRelevant'].values

    test_text = data.iloc[test_indices]['pos_tag'].values
    test_y = data.iloc[test_indices]['isRelevant'].values

    rf_pipeline.fit(train_text, train_y)
    predictions = rf_pipeline.predict(test_text)

    rf_conf_mat += confusion_matrix(test_y, predictions)
    score1 = f1_score(test_y, predictions)
    rf_f1_scores.append(score1)
    score2 = accuracy_score(test_y, predictions)
    rf_ac_scores.append(score2)
    score3 = precision_score(test_y, predictions)
    rf_pr_scores.append(score3)
    score4 = recall_score(test_y, predictions)
    rf_re_scores.append(score4)

print("\nPrinting Results for Random Forest Model...")
print("Comments Classified: ", len(data))
print("F1 Score: ", sum(rf_f1_scores)/len(rf_f1_scores))
print("Accuracy Score: ", sum(rf_ac_scores)/len(rf_ac_scores))
print("Precision Score: ", sum(rf_pr_scores)/len(rf_pr_scores))
print("Recall Score: ", sum(rf_re_scores)/len(rf_re_scores))
print("Confusion Matrix: ")
print(rf_conf_mat)

######### DECISION TREE MODEL #########

dt_pipeline = Pipeline([
    ('vectorizer', CountVectorizer(ngram_range = (1, 3))),
    ('tfidf_transformer', TfidfTransformer()),
    ('classifier', DecisionTreeClassifier())
])

k_fold = KFold(n_splits = 10)
dt_f1_scores = []
dt_ac_scores = []
dt_pr_scores = []
dt_re_scores = []
dt_conf_mat = np.array([[0, 0], [0, 0]])

for train_indices, test_indices in k_fold.split(data):

    train_text = data.iloc[train_indices]['pos_tag'].values
    train_y = data.iloc[train_indices]['isRelevant'].values

    test_text = data.iloc[test_indices]['pos_tag'].values
    test_y = data.iloc[test_indices]['isRelevant'].values

    dt_pipeline.fit(train_text, train_y)
    predictions = dt_pipeline.predict(test_text)

    dt_conf_mat += confusion_matrix(test_y, predictions)
    score1 = f1_score(test_y, predictions)
    dt_f1_scores.append(score1)
    score2 = accuracy_score(test_y, predictions)
    dt_ac_scores.append(score2)
    score3 = precision_score(test_y, predictions)
    dt_pr_scores.append(score3)
    score4 = recall_score(test_y, predictions)
    dt_re_scores.append(score4)

print("\nPrinting Results for Decision Tree Model...")
print("Comments Classified: ", len(data))
print("F1 Score: ", sum(dt_f1_scores)/len(dt_f1_scores))
print("Accuracy Score: ", sum(dt_ac_scores)/len(dt_ac_scores))
print("Precision Score: ", sum(dt_pr_scores)/len(dt_pr_scores))
print("Recall Score: ", sum(dt_re_scores)/len(dt_re_scores))
print("Confusion Matrix: ")
print(dt_conf_mat)

end_time = time()
time_taken = end_time - start_time

print("Total time taken in seconds: ", time_taken)
