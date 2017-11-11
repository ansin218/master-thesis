import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.naive_bayes import MultinomialNB
from sklearn.linear_model import LogisticRegression
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

print(np.bincount(labels))

count_vectorizer = CountVectorizer()
counts = count_vectorizer.fit_transform(texts)

classifier = MultinomialNB()
targets = labels
classifier.fit(counts, targets)

#examples = ["+1", "Nice"]
#example_counts = count_vectorizer.transform(examples)
#predictions = classifier.predict(example_counts)
#print(predictions)

nb_pipeline = Pipeline([
    ('vectorizer', CountVectorizer(ngram_range = (1, 10))),
    ('tfidf_transformer', TfidfTransformer()),
    ('classifier', MultinomialNB())
])

#pipeline.fit(texts, labels)
#pipeline.predict(examples)

k_fold = KFold(n_splits = 10)
nb_scores = []
#conf_mat = np.array([[0, 0], [0, 0]])

for train_indices, test_indices in k_fold.split(data):

    train_text = data.iloc[train_indices]['sentence'].values
    train_y = data.iloc[train_indices]['isRelevant'].values

    test_text = data.iloc[test_indices]['sentence'].values
    test_y = data.iloc[test_indices]['isRelevant'].values

    nb_pipeline.fit(train_text, train_y)
    predictions = nb_pipeline.predict(test_text)

    #conf_mat += confusion_matrix(test_y, predictions)
    score = f1_score(test_y, predictions)
    nb_scores.append(score)

print("Comments Classified: ", len(data))
print("Accuracy Score: ", sum(nb_scores)/len(nb_scores))
#print("Confusion Matrix: ")
#print(conf_mat)

logit_pipeline = Pipeline([
    ('vectorizer', CountVectorizer(ngram_range = (1, 10))),
    ('tfidf_transformer', TfidfTransformer()),
    ('classifier', LogisticRegression())
])

logit_scores = []

for train_indices, test_indices in k_fold.split(data):

    train_text = data.iloc[train_indices]['sentence'].values
    train_y = data.iloc[train_indices]['isRelevant'].values

    test_text = data.iloc[test_indices]['sentence'].values
    test_y = data.iloc[test_indices]['isRelevant'].values

    logit_pipeline.fit(train_text, train_y)
    predictions = logit_pipeline.predict(test_text)

    #conf_mat += confusion_matrix(test_y, predictions)
    score = f1_score(test_y, predictions)
    logit_scores.append(score)

print("Comments Classified: ", len(data))
print("Accuracy Score: ", sum(logit_scores)/len(logit_scores))
