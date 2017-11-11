import pandas as pd
import numpy as np
from time import time
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.naive_bayes import MultinomialNB
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import Perceptron
from sklearn.linear_model import SGDClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.pipeline import Pipeline
from sklearn.model_selection import KFold
from sklearn.metrics import confusion_matrix, accuracy_score, f1_score, precision_score, recall_score

start_time = time()

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
nb_f1_scores = []
nb_ac_scores = []
nb_pr_scores = []
nb_re_scores = []
nb_conf_mat = np.array([[0, 0], [0, 0]])

for train_indices, test_indices in k_fold.split(data):

    train_text = data.iloc[train_indices]['sentence'].values
    train_y = data.iloc[train_indices]['isRelevant'].values

    test_text = data.iloc[test_indices]['sentence'].values
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

######### LOGISTIC REGRESSION MODEL #########

logit_pipeline = Pipeline([
    ('vectorizer', CountVectorizer(ngram_range = (1, 10))),
    ('tfidf_transformer', TfidfTransformer()),
    ('classifier', LogisticRegression())
])

logit_f1_scores = []
logit_ac_scores = []
logit_pr_scores = []
logit_re_scores = []
logit_conf_mat = np.array([[0, 0], [0, 0]])

for train_indices, test_indices in k_fold.split(data):

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

print("\nPrinting Results for Logistic Regression Model...")
print("Comments Classified: ", len(data))
print("F1 Score: ", sum(logit_f1_scores)/len(logit_f1_scores))
print("Accuracy Score: ", sum(logit_ac_scores)/len(logit_ac_scores))
print("Precision Score: ", sum(logit_pr_scores)/len(logit_pr_scores))
print("Recall Score: ", sum(logit_re_scores)/len(logit_re_scores))
print("Confusion Matrix: ")
print(logit_conf_mat)

######### SUPPORT VECTOR MACHINES MODEL #########

svc_pipeline = Pipeline([
    ('vectorizer', CountVectorizer(ngram_range = (1, 10))),
    ('tfidf_transformer', TfidfTransformer()),
    ('classifier', SVC())
])

svc_f1_scores = []
svc_ac_scores = []
svc_pr_scores = []
svc_re_scores = []
svc_conf_mat = np.array([[0, 0], [0, 0]])

for train_indices, test_indices in k_fold.split(data):

    train_text = data.iloc[train_indices]['sentence'].values
    train_y = data.iloc[train_indices]['isRelevant'].values

    test_text = data.iloc[test_indices]['sentence'].values
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
    ('vectorizer', CountVectorizer(ngram_range = (1, 10))),
    ('tfidf_transformer', TfidfTransformer()),
    ('classifier', RandomForestClassifier())
])

rf_f1_scores = []
rf_ac_scores = []
rf_pr_scores = []
rf_re_scores = []
rf_conf_mat = np.array([[0, 0], [0, 0]])

for train_indices, test_indices in k_fold.split(data):

    train_text = data.iloc[train_indices]['sentence'].values
    train_y = data.iloc[train_indices]['isRelevant'].values

    test_text = data.iloc[test_indices]['sentence'].values
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
    ('vectorizer', CountVectorizer(ngram_range = (1, 10))),
    ('tfidf_transformer', TfidfTransformer()),
    ('classifier', RandomForestClassifier())
])

dt_f1_scores = []
dt_ac_scores = []
dt_pr_scores = []
dt_re_scores = []
dt_conf_mat = np.array([[0, 0], [0, 0]])

for train_indices, test_indices in k_fold.split(data):

    train_text = data.iloc[train_indices]['sentence'].values
    train_y = data.iloc[train_indices]['isRelevant'].values

    test_text = data.iloc[test_indices]['sentence'].values
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

######### STOCHASTIC GRADIENT DESCENT MODEL #########

sgdc_pipeline = Pipeline([
    ('vectorizer', CountVectorizer(ngram_range = (1, 10))),
    ('tfidf_transformer', TfidfTransformer()),
    ('classifier', SGDClassifier())
])

sgdc_f1_scores = []
sgdc_ac_scores = []
sgdc_pr_scores = []
sgdc_re_scores = []
sgdc_conf_mat = np.array([[0, 0], [0, 0]])

for train_indices, test_indices in k_fold.split(data):

    train_text = data.iloc[train_indices]['sentence'].values
    train_y = data.iloc[train_indices]['isRelevant'].values

    test_text = data.iloc[test_indices]['sentence'].values
    test_y = data.iloc[test_indices]['isRelevant'].values

    sgdc_pipeline.fit(train_text, train_y)
    predictions = sgdc_pipeline.predict(test_text)

    sgdc_conf_mat += confusion_matrix(test_y, predictions)
    score1 = f1_score(test_y, predictions)
    sgdc_f1_scores.append(score1)
    score2 = accuracy_score(test_y, predictions)
    sgdc_ac_scores.append(score2)
    score3 = precision_score(test_y, predictions)
    sgdc_pr_scores.append(score3)
    score4 = recall_score(test_y, predictions)
    sgdc_re_scores.append(score4)

print("\nPrinting Results for Stochastic Gradient Descent Model...")
print("Comments Classified: ", len(data))
print("F1 Score: ", sum(sgdc_f1_scores)/len(sgdc_f1_scores))
print("Accuracy Score: ", sum(sgdc_ac_scores)/len(sgdc_ac_scores))
print("Precision Score: ", sum(sgdc_pr_scores)/len(sgdc_pr_scores))
print("Recall Score: ", sum(sgdc_re_scores)/len(sgdc_re_scores))
print("Confusion Matrix: ")
print(sgdc_conf_mat)

######### PERCEPTRON MODEL #########

perceptron_pipeline = Pipeline([
    ('vectorizer', CountVectorizer(ngram_range = (1, 10))),
    ('tfidf_transformer', TfidfTransformer()),
    ('classifier', Perceptron())
])

perceptron_f1_scores = []
perceptron_ac_scores = []
perceptron_pr_scores = []
perceptron_re_scores = []
perceptron_conf_mat = np.array([[0, 0], [0, 0]])

for train_indices, test_indices in k_fold.split(data):

    train_text = data.iloc[train_indices]['sentence'].values
    train_y = data.iloc[train_indices]['isRelevant'].values

    test_text = data.iloc[test_indices]['sentence'].values
    test_y = data.iloc[test_indices]['isRelevant'].values

    perceptron_pipeline.fit(train_text, train_y)
    predictions = perceptron_pipeline.predict(test_text)

    perceptron_conf_mat += confusion_matrix(test_y, predictions)
    score1 = f1_score(test_y, predictions)
    perceptron_f1_scores.append(score1)
    score2 = accuracy_score(test_y, predictions)
    perceptron_ac_scores.append(score2)
    score3 = precision_score(test_y, predictions)
    perceptron_pr_scores.append(score3)
    score4 = recall_score(test_y, predictions)
    perceptron_re_scores.append(score4)

print("\nPrinting Results for Perceptron Model...")
print("Comments Classified: ", len(data))
print("F1 Score: ", sum(perceptron_f1_scores)/len(perceptron_f1_scores))
print("Accuracy Score: ", sum(perceptron_ac_scores)/len(perceptron_ac_scores))
print("Precision Score: ", sum(perceptron_pr_scores)/len(perceptron_pr_scores))
print("Recall Score: ", sum(perceptron_re_scores)/len(perceptron_re_scores))
print("Confusion Matrix: ")
print(perceptron_conf_mat)

######### K-NEIGHBORS CLASSIFIER MODEL #########

knn_pipeline = Pipeline([
    ('vectorizer', CountVectorizer(ngram_range = (1, 10))),
    ('tfidf_transformer', TfidfTransformer()),
    ('classifier', KNeighborsClassifier())
])

knn_f1_scores = []
knn_ac_scores = []
knn_pr_scores = []
knn_re_scores = []
knn_conf_mat = np.array([[0, 0], [0, 0]])

for train_indices, test_indices in k_fold.split(data):

    train_text = data.iloc[train_indices]['sentence'].values
    train_y = data.iloc[train_indices]['isRelevant'].values

    test_text = data.iloc[test_indices]['sentence'].values
    test_y = data.iloc[test_indices]['isRelevant'].values

    knn_pipeline.fit(train_text, train_y)
    predictions = knn_pipeline.predict(test_text)

    knn_conf_mat += confusion_matrix(test_y, predictions)
    score1 = f1_score(test_y, predictions)
    knn_f1_scores.append(score1)
    score2 = accuracy_score(test_y, predictions)
    knn_ac_scores.append(score2)
    score3 = precision_score(test_y, predictions)
    knn_pr_scores.append(score3)
    score4 = recall_score(test_y, predictions)
    knn_re_scores.append(score4)

print("\nPrinting Results for K-Neighbors Classifier Model...")
print("Comments Classified: ", len(data))
print("F1 Score: ", sum(knn_f1_scores)/len(knn_f1_scores))
print("Accuracy Score: ", sum(knn_ac_scores)/len(knn_ac_scores))
print("Precision Score: ", sum(knn_pr_scores)/len(knn_pr_scores))
print("Recall Score: ", sum(knn_re_scores)/len(knn_re_scores))
print("Confusion Matrix: ")
print(knn_conf_mat)

end_time = time()
time_taken = end_time - start_time

print("Total time taken in seconds: ", time_taken)
