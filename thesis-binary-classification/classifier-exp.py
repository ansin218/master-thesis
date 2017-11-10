import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.feature_extraction.text import CountVectorizer

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
