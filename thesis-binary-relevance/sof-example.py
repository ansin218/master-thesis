from sklearn.datasets import make_classification
from sklearn.cross_validation import cross_val_predict
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import classification_report

# generate some artificial data with 11 classes
X, y = make_classification(n_samples=2000, n_features=20, n_informative=10, n_classes=11, random_state=0)

# your classifier, assume GaussianNB here for non-integer data X
estimator = GaussianNB()
# generate your cross-validation prediction with 10 fold Stratified sampling
y_pred = cross_val_predict(estimator, X, y, cv=10)

# generate report
print(classification_report(y, y_pred))