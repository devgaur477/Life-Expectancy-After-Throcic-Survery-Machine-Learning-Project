import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import csv
pd.options.mode.chained_assignment = None  # default='warn'
# Importing the dataset
dataset = pd.read_csv('final_data.csv')

X = dataset.iloc[1:400, 6:15].values
y = dataset.iloc[1:400 ,  -1].values


# Splitting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.25, random_state = 0)

# Feature Scaling
# from sklearn.preprocessing import StandardScaler
# sc = StandardScaler()
# X_train = sc.fit_transform(X_train)
# X_test = sc.transform(X_test)


# Training the Random Forest Classification model on the Training set
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import RandomForestRegressor
# classifier = RandomForestClassifier(n_estimators = 10, criterion = 'entropy', random_state = 0)
# classifier.fit(X_train, y_train)
regressor = RandomForestRegressor(n_estimators = 10, random_state = 0)
regressor.fit(X, y)


# Predicting a new result
y_pred = regressor.predict(X_test)


# Predicting the Test set results
#y_pred = classifier.reg(X_test)

#y_final = round(y_pred)
#y_final = np.array(b).round
y = np.round(y_pred)
print(y)





from sklearn.metrics import accuracy_score, precision_score , recall_score,f1_score



a = accuracy_score(y_test, y)

print(a)
pscore = precision_score(y_test , y , average = 'weighted')

# print(pscore)

rscore = recall_score(y_test , y, average='weighted')
# print(a)

fscore =f1_score(y_test, y, labels=None, pos_label=1, average='weighted', sample_weight=None, zero_division='warn')

# print(fscore)


plt.scatter(y_test, y_pred, color = 'red')
plt.hist(y)
# plt.plot(y_test, regressor.predict(X_test), color = 'blue')
plt.title('')
plt.xlabel('')
plt.ylabel('')
plt.show()
