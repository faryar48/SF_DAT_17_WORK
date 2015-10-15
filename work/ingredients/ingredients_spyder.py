# -*- coding: utf-8 -*-
"""
Created on Wed Oct 14 19:45:00 2015

@author: faryarghaemi
"""

import pandas as pd
import json
from collections import Counter 


json_data = open('train.json').read()
data = pd.read_json(json_data)
data.head()
data.describe()

unique_ingredients = []
for x in data.ingredients:
   for y in x:
       if y in unique_ingredients:
           pass
       else:
           unique_ingredients.append(y)
           
           
unique_cuisines = []
for x in data.cuisine:
   if x in unique_cuisines:
       pass
   else:
       unique_cuisines.append(x)         

unique_ingredients[:20]
unique_cuisines

for i in unique_ingredients:
    data[i] = 0

cuisine_with_ingredients = {}
for cuisine in unique_cuisines: 
    cuisine_with_ingredients[cuisine] = []
    
    
for ingredient_set in data.ingredients:
    print ingredient_set
    
    
data.cuisine[0]
data.ingredients[0]
data.head()


 
ingredients_by_cuisine = data['data.ingredients'].groupby('unique_cuisines')

final_array = []
for cuisine in unique_cuisines:
    cuisine_array = [cuisine]
    print cuisine_array
    for ingredient in unique_ingredients:
        print ingredient 
        ingredient_count = {}
        if ingredient in unique_ingredients:
            if ingredient in ingredient_count: 
                ingredient_count[ingredient] += 1
            else: 
                ingredient_count[ingredient] = 1 
    cuisine_array.append(ingredient_count)
    final_array.append(cuisine)

final_array 

    