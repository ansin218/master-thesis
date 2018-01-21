import pandas as pd
import numpy as np
from time import time
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from skmultilearn.problem_transform import BinaryRelevance
from sklearn.ensemble import RandomForestClassifier
from sklearn.pipeline import Pipeline
from sklearn.model_selection import KFold
from sklearn.metrics import confusion_matrix, accuracy_score, f1_score, precision_score, recall_score

start_time = time()

data = pd.read_csv("a_lucene_results.csv")

######### RANDOM FOREST MODEL #########

rf_pipeline = Pipeline([
    ('vectorizer', CountVectorizer()),
    ('tfidf_transformer', TfidfTransformer()),
    ('classifier', BinaryRelevance(RandomForestClassifier()))
])

k_fold = KFold(n_splits = 10)
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

end_time = time()
time_taken = end_time - start_time

print("Total time taken in seconds: ", time_taken)
