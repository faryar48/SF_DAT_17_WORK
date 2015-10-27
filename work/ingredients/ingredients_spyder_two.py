# -*- coding: utf-8 -*-
"""
Created on Thu Oct 15 12:37:57 2015

@author: faryarghaemi
"""

# PREDICTING CUISINE TYPE FROM FOOD INGREDIENTS
import pandas as pd
import json
from collections import Counter
import seaborn as sns
import matplotlib.pyplot as plt
%matplotlib inline

# READ IN JSON DATA TO DF
json_data = open('train.json').read()
data = pd.read_json(json_data)
data.head()

# create list of most common ingredients
all_ingredients = reduce(lambda x,y: x+y, list(data.ingredients))
len(all_ingredients) # 428275
   
# create unique list of ingredients
unique_ingredients = set(all_ingredients)


# setting true or false if ingredient appears in food_type 
def ingredient_in_food(food, ingredient):
  return ingredient in food

for i in unique_ingredients:
  data[i] = data.ingredients.apply(lambda x: ingredient_in_food(x, i))
  

# set feature columns
feature_cols = list(unique_ingredients)

#frequent cuisine
#less_frequent = [x for x in feature_cols if x not in most_frequent]
X = data[feature_cols]
y = data.cuisine

# plot the data 
# sns.pairplot(data, X, y, size = 6, aspect = 0.6)

# TEST ENVIRONMENT
# create test / train split
from sklearn.cross_validation import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=1)

# run log reg & get coefs
from sklearn.linear_model import LogisticRegression
logreg = LogisticRegression()
logreg.fit(X_train, y_train)
zip(feature_cols, logreg.coef_[0])

# prediction accuracy
from sklearn import metrics
y_pred = logreg.predict(X_test)
print metrics.accuracy_score(y_test, y_pred)