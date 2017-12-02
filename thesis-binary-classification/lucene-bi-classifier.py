# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np
from time import time
from sklearn.linear_model import LogisticRegression
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.pipeline import Pipeline
from sklearn.model_selection import KFold
from sklearn.metrics import confusion_matrix, accuracy_score, f1_score, precision_score, recall_score

start_time = time()

data = pd.read_csv("a_lucene_results.csv")

######### LOGISTIC REGRESSION MODEL #########

logit_pipeline = Pipeline([
    #('vectorizer', CountVectorizer(ngram_range = (1, 10))),
    #('tfidf_transformer', TfidfTransformer()),
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
        train_text = data.iloc[train_indices]['sentence'].values
        train_y = data.iloc[train_indices]['isRelevant'].values

        test_text = data.iloc[test_indices]['sentence'].values
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

end_time = time()
time_taken = end_time - start_time

print("Total time taken in seconds: ", time_taken)
