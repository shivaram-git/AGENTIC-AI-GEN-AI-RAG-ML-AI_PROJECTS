# -*- coding: utf-8 -*-
"""
Created on Sat Oct 10 17:12:07 2026

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

from sklearn.tree import DecisionTreeClassifier
classifier = DecisionTreeClassifier(max_depth = 4,splitter='random')
classifier.fit(X_train,y_train)

from sklearn.ensemble import RandomForestClassifier
classifier = RandomForestClassifier(
                max_depth = 4,
                n_estimators = 30,
                criterion = 'entropy',
                random_state = 0
    )
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

