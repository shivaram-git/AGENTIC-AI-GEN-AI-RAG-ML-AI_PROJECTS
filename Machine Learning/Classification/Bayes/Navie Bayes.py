# -*- coding: utf-8 -*-
"""
Created on Fri Oct  9 17:32:00 2026

@author: SHIVARAM
"""

# -*- coding: utf-8 -*-
"""
Created on Mon Oct  5 17:10:53 2026

@author: SHIVARAM
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

dataset = pd.read_csv(r"C:\Users\SHIVARAM\OneDrive\Desktop\FSDS\Machine Learning\Classification\logit classification.csv")





X = dataset.iloc[:,[2,3]].values
y = dataset.iloc[:,-1].values


from sklearn.model_selection import train_test_split

X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2,random_state=0)

from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test= sc.transform(X_test)


# Train the model X_train, Y_train

from sklearn.naive_bayes import BernoulliNB
classifier = BernoulliNB()
classifier.fit(X_train,y_train)


from sklearn.naive_bayes import GaussianNB
classifier = GaussianNB()
classifier.fit(X_train,y_train)


# create prediction for x_test

y_pred = classifier.predict(X_test)


from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test,y_pred)
print(cm)

# THis is to get model accuracy

from sklearn.metrics import accuracy_score
ac = accuracy_score(y_test,y_pred)
print(ac)


from sklearn.metrics import classification_report
cr = classification_report(y_test,y_pred)

print(cr)

bias = classifier.score(X_train,y_train)
print(bias)

variance = classifier.score(X_test,y_test)
print(variance)


# Future prediction

dataset1 = pd.read_csv(r"C:\Users\SHIVARAM\OneDrive\Desktop\FSDS\Machine Learning\Classification\final.csv")

d2 = dataset1.copy()
dataset1 = dataset1.iloc[:,[3,4]].values 

from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
M = sc.fit_transform(dataset1)

y_pred1 = pd.DataFrame()
d2 ['y_pred1'] = classifier.predict(M)

d2.to_csv('final.csv')























