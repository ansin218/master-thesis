import numpy as np
from sklearn.metrics import accuracy_score
from sklearn.datasets import fetch_mldata
from skmultilearn.problem_transform import BinaryRelevance
from sklearn.ensemble import RandomForestClassifier

data = fetch_mldata('yeast')
X = data.data
y = data.target.toarray().astype(np.int).T

clf = BinaryRelevance(RandomForestClassifier())
clf.fit(X, np.array(y))
y_pred = clf.predict(X)

print(accuracy_score(y, y_pred))
