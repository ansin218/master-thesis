import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
from sklearn.cross_validation import KFold
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

examples = ["+1", "Nice"]
example_counts = count_vectorizer.transform(examples)
predictions = classifier.predict(example_counts)
print(predictions)

pipeline = Pipeline([
    ('vectorizer', CountVectorizer()),
    ('classifier', MultinomialNB())
])

pipeline.fit(texts, labels)
print(pipeline.predict(examples))
