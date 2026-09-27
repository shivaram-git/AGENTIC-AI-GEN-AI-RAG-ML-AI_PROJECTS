# -*- coding: utf-8 -*-
"""
Created on Wed Sep 23 17:04:55 2026

@author: SHIVARAM
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

dataset = pd.read_csv(r"C:\Users\SHIVARAM\OneDrive\Desktop\FSDS\Machine Learning\Salary_Data.csv")

x = dataset.iloc[:,:-1]
y = dataset.iloc[:,-1]

from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test = train_test_split(x,y,test_size=0.2,random_state=0)


from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X_train,y_train)

print(regressor)  # regressor is a ml model which conside linear regression algorithm

print(regressor.get_params())


y_pred = regressor.predict(X_test)

comparision = pd.DataFrame({'Actual':y_test,'Prediction':y_pred})
print(comparision)






plt.scatter(X_test, y_test, color = 'red')
plt.plot(X_train,regressor.predict(X_train),color = 'blue')
plt.title('Salary vs Expreince')
plt.xlabel('Exp')
plt.ylabel('Salary')
plt.show()







































































































