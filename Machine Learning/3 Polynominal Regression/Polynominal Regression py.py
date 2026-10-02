# -*- coding: utf-8 -*-
"""
Created on Thu Oct  1 16:34:39 2026

@author: SHIVARAM
"""
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

dataset = pd.read_csv(r"D:\Downloads\emp_sal.csv")


X = dataset.iloc[:,1:2].values
y = dataset.iloc[:,2].values


#linear regression model

from sklearn.linear_model import LinearRegression
lr = LinearRegression()
lr.fit(X,y)

# linear regression visualization

plt.scatter(X,y,color = 'red')
plt.plot(X,lr.predict(X),color = 'blue')
plt.title('Linear Regression graph')
plt.xlabel('Position graph')
plt.ylabel('Salary')
plt.show()


from sklearn.preprocessing import PolynomialFeatures
poly_reg = PolynomialFeatures(degree = 5)
X_poly = poly_reg.fit_transform(X)

poly_reg.fit(X_poly,y)
lin_reg2 = LinearRegression()
lin_reg2.fit(X_poly,y)


plt.scatter(X,y,color = 'red')
plt.plot(X,lin_reg2.predict(poly_reg.fit_transform(X)),color='blue')
plt.title('Level or Salary(Polynomial Regression)')
plt.xlabel('Position Level')
plt.ylabel('Salary')
plt.show()


lin_model_pred = lr.predict([[6.5]])
lin_model_pred

poly_model_reg = lin_reg2.predict(poly_reg.fit_transform([[6.5]]))

poly_model_reg




# SVR MOdel

from sklearn.svm import SVR
svr_reg = SVR(kernel='poly',degree=4,gamma='auto')
svr_reg.fit(X,y)

svr_model_pred = svr_reg.predict([[6.5]])
svr_model_pred



















