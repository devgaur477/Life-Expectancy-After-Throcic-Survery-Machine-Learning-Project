# Kernel SVM

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import csv
pd.options.mode.chained_assignment = None  # default='warn'
# Importing the dataset
dataset = pd.read_csv('final_data2.csv')

X = dataset.iloc[1:400, 6:15].values
y = dataset.iloc[1:400, -1].values


# Splitting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.25, random_state = 0)


# # Feature Scaling
# from sklearn.preprocessing import StandardScaler
# sc_X = StandardScaler()
# sc_y = StandardScaler()
# X = sc_X.fit_transform(X)
# y = sc_y.fit_transform(y)


# Training the Kernel SVM model on the Training set
from sklearn.svm import SVC
classifier = SVC(kernel = 'rbf', random_state = 2)
classifier.fit(X_train, y_train)
# from sklearn.svm import SVR
# regressor = SVR(kernel = 'linear')
# regressor.fit(X, y)


# Predicting the Test set results
y_pred = classifier.predict(X_test)

y = np.round(y_pred)



# Making the Confusion Matrix
from sklearn.metrics import confusion_matrix , precision_score , recall_score
# cm = confusion_matrix(y_test, y_pred)

from sklearn.metrics import accuracy_score , recall_score , f1_score

a = accuracy_score(y_test, y)



pscore = precision_score(y_test , y , average = 'weighted')

rscore = recall_score(y_test , y, average='weighted')
print(a)

#print(pscore)

# print(rscore)

fscore =f1_score(y_test, y, labels=None, pos_label=1, average='weighted', sample_weight=None, zero_division='warn')

# print(fscore)



