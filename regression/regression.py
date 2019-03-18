#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan  7 13:45:37 2019

@author: aiktc
"""

import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt

dataset = pd.read_csv('Salary_Data.csv')
X = dataset.iloc[:,:-1]
y = dataset.iloc[:,1]

from sklearn.model_selection import train_test_split

X_train,X_test,y_train,y_test = train_test_split(X,y,test_size = 1/3,random_state = 0)

from sklearn.linear_model import LinearRegression

regressor = LinearRegression()
regressor.fit(X_train,y_train)

y_pred = regressor.predict(X_test)


plt.scatter(X_train,y_train,color='red')
plt.plot(X_train,regressor.predict(X_train),color='blue')
plt.title('Salary vs Experience(Training set)')
plt.xlabel('Years of Explerince')
plt.ylabel('Salary')
plt.show()

plt.scatter(X_train,y_train,color='green')
plt.plot(X_train,regressor.predict(X_train),color='yellow')
plt.title('Salary vs Experience(Testing set)')
plt.xlabel('Years of Explerince')
plt.ylabel('Salary')
plt.show()