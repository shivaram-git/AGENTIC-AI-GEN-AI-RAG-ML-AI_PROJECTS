# -*- coding: utf-8 -*-
"""
Created on Fri Sep 25 16:38:44 2026

@author: SHIVARAM
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

dataset = pd.read_csv(r"C:\Users\SHIVARAM\OneDrive\Desktop\FSDS\Machine Learning\MultipleLinear Regreession\Investment.csv")

X = dataset.iloc[:,:-1]
y = dataset.iloc[:,4]

X = pd.get_dummies(X,dtype=int)

from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2,random_state=0)

from sklearn.linear_model import LinearRegression

regresssor = LinearRegression()
regresssor.fit(X_train,y_train)


y_pred = regresssor.predict(X_test)

m = regresssor.coef_
print(m)

c = regresssor.intercept_
print(c)

X = np.append(arr = np.full((50,1),42467).astype(int) ,values = X , axis = 1)


# feature elimination technique

import statsmodels.api as sm
X_opt = X[:,[0,1,2,3,4,5]]

regressor_OLS = sm.OLS(endog = y,exog = X_opt).fit()
regressor_OLS.summary()


import statsmodels.api as sm
X_opt = X[:,[0,1,2,3,5]]

regressor_OLS = sm.OLS(endog = y,exog = X_opt).fit()
regressor_OLS.summary()



import statsmodels.api as sm
X_opt = X[:,[0,1,2,3]]

regressor_OLS = sm.OLS(endog = y,exog = X_opt).fit()
regressor_OLS.summary()



import statsmodels.api as sm
X_opt = X[:,[0,1]]

regressor_OLS = sm.OLS(endog = y,exog = X_opt).fit()
regressor_OLS.summary()






























