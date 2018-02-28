#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 17 12:20:21 2018

@author: crazytrau
"""
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#import dataset
dataset = pd.read_csv('Data.csv')
X = dataset.iloc[:,0:3].values
Y = dataset.iloc[:,3].values

## take care of missing values
#from sklearn.preprocessing import Imputer
#imputer = Imputer(missing_values = 'NaN', strategy='mean', axis=0, verbose=0, copy=True)
#imputer = imputer.fit(X[:,1:3])
#X[:,1:3] = imputer.transform(X[:,1:3])
#
## encoding categorical data
#from sklearn.preprocessing import LabelEncoder, OneHotEncoder
#labelencoder = LabelEncoder()
#X[:,0] = labelencoder.fit_transform(X[:,0])
#onehotencoder_x = OneHotEncoder(categorical_features=[0])
#X = onehotencoder_x.fit_transform(X).toarray()
#labelencoder_y = LabelEncoder()
#y= labelencoder_y.fit_transform(Y)

#splitting dataset to training set and test set
from sklearn.cross_validation import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

## Feature scaling
#from sklearn.preprocessing import StandardScaler
#sc_X = StandardScaler()
#X_train = sc_X.fit_transform(X_train)
#X_test = sc_X.transform(X_test)
