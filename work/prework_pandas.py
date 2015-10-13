# -*- coding: utf-8 -*-
"""
Created on Fri Sep 18 09:52:43 2015

@author: faryarghaemi
"""
from pandas import DataFrame, read_csv 

import matplotlib.pyplot as plt
import pandas as pd
import sys 
%matplotlib inline

print 'Python version ' + sys.version
print 'Pandas version ' + pd.__version__

names = ['Bob', 'Jessica', 'Mary', 'John', 'Mel']
births = [968, 155, 77, 578, 973]

BabyDataSet = zip(names, births)
BabyDataSet

# df will be a DataFrame object. You can think of this object holding the contents of the BabyDataSet in a format similar to a sql table or an excel spreadsheet. Lets take a look below at the contents inside df.
df = pd.DataFrame(data = BabyDataSet, columns = ['Names', 'Births' ])
df

df.to_csv('births1880.csv',index=False,header=False)

# Notice the r before the string. Since the slashes are special characters, prefixing the string with a r will escape the whole string.
Location = r'/Users/faryarghaemi/Desktop/EVERYDAY/dat-17/SF_DAT_17_WORK/births1880.csv'
df = pd.read_csv(Location)
df 

# The read_csv function treated the first record in the csv file as the header names. This is obviously not correct since the text file did not provide us with header names.
# To correct this we will pass the header parameter to the read_csv function and set it to None (means null in python).
Location = r'/Users/faryarghaemi/Desktop/EVERYDAY/dat-17/SF_DAT_17_WORK/births1880.csv'
df = pd.read_csv(Location, header=None)
df 

# If we wanted to give the columns specific names, we would have to pass another paramter called names. We can also omit the header parameter.
df = pd.read_csv(Location, names=['Names', 'Births'])
df

# Delete the csv file now that we are done using it.
import os
os.remove(Location)

# Check the data type o the columns
df.dtypes 

# Check the data type of Births column
df.Births.dtype 

# To find the most popular name or the baby name with the higest birth rate, we can do one of the following.
# Method 1:  
Sorted = df.sort(['Births'], ascending=False)
Sorted.head(1)

# Method 2: 
df['Births'].max()

# Create a graph 
df['Births'].plot()

# Max value in the data set 
MaxValue = df['Births'].max()

# Name associated with the max value 
MaxName = df['Names'][df['Births'] == df['Births'].max()].values 

# Text to display on graph 
Text = str(MaxValue) + " - " + MaxName

# Add text to the graph
plt.annotate(Text, xy=(1, MaxValue), xytext=(8, 0), 
                 xycoords=('axes fraction', 'data'), textcoords='offset points')
                 
print "The most popular name"
df[df['Births'] == df['Births'].max()]
# Sorted.head(1) can also be used 


# LESSON 2 LESSON 2 LESSON 2 LESSON 2 LESSON 2 LESSON 2 LESSON 2 LESSON 2 

from numpy import random 
random.seed(500)
random_names = [names[random.randint(low=0,high=len(names))] for i in range(1000)]

# Print first 10 records 
random_names[:10]

# The number of births per name for the year 1880 
births = [random.randint(low=0,high=1000) for i in range(1000)]
births[:10]

# Merge datasets 

BabyDataSet = zip(random_names, births)
BabyDataSet[:10]

df = pd.DataFrame(data = BabyDataSet, columns=['Names', 'Births'])
df[:10]

df.to_csv('births1880.txt',index=False,header=False)

Location = r'/Users/faryarghaemi/Desktop/EVERYDAY/dat-17/SF_DAT_17_WORK/births1880.txt'
df = pd.read_csv(Location)

df.info()

# To actually see the contents of the dataframe we can use the head() function which by default will return the first five records. You can also pass in a number n to return the top n records of the dataframe.
df.head()

df = pd.read_csv(Location, header=None)
df.info()

df.tail()

df = pd.read_csv(Location, names=['Names', 'Births'])
df.head()

import os 
os.remove(Location)

# We can use the unique property of the dataframe to find all the unique records of the "Names" column. 
# Method 1: 
df['Names'].unique()

# If you actually want to print the unique value s: 
for x in df['Names'].unique():
    print x
    
# Method 2:
print df['Names'].describe()
    
# Since we have multiple values per baby name, we need to aggregate this data so we only have a baby name appear once. This means the 1,000 rows will need to become 5. We can accomplish this by using the groupby function.
# Create a groupby object 
name = df.groupby('Names')

# Apply the same function to the groupby object 
df = name.sum()
df

# To find the most popular name or the baby name with the higest birth rate, we can do one of the following.
# Sort the dataframe and select the top row
# Use the max() attribute to find the maximum value

# Method 1 
Sorted = df.sort(['Births'], ascending=False)
Sorted.head(1)

# Method 2 
df['Births'].max()

# Create graph 
df['Births'].plot(kind='bar')

print 'The most popular name'
df.sort(columns='Births', ascending=False)

# LESSON 3 LESSON 3 LESSON 3 LESSON 3 LESSON 3 LESSON 3 LESSON 3 LESSON 3 
from numpy import random 

# Import libraries
import pandas as pd
import matplotlib.pyplot as plt
import numpy.random as np
import sys

print 'Python version ' + sys.version
print 'Pandas version: ' + pd.__version__

%matplotlib inline
# set seed
np.seed(111)

# Function to generate test data
def CreateDataSet(Number=1):
    
    Output = []
    
    for i in range(Number):
        
        # Create a weekly (mondays) date range
        rng = pd.date_range(start='1/1/2009', end='12/31/2012', freq='W-MON')
        
        # Create random data
        data = np.randint(low=25,high=1000,size=len(rng))
        
        # Status pool
        status = [1,2,3]
        
        # Make a random list of statuses
        random_status = [status[np.randint(low=0,high=len(status))] for i in range(len(rng))]
        
        # State pool
        states = ['GA','FL','fl','NY','NJ','TX']
        
        # Make a random list of states 
        random_states = [states[np.randint(low=0,high=len(states))] for i in range(len(rng))]
    
        Output.extend(zip(random_states, random_status, data, rng))
        
    return Output
        
dataset = CreateDataSet(4)
df = pd.DataFrame(data=dataset, columns=['State','Status','CustomerCount','StatusDate'])
df.info()

df.head()

# Save results to excel 
df.to_excel('Lesson3.xlsx', index=False)
print 'Done'
        
# Location of file        
Location = r'/Users/faryarghaemi/Desktop/EVERYDAY/dat-17/SF_DAT_17_WORK/Lesson3.xlsx'

# Parse a specific sheet 
df = pd.read_excel(Location, 0, index_col='StatusDate')
df.dtypes

df.index

df.head()

df['State'].unique()

# Clean State Column, convert to upper case
df['State'] = df.State.apply(lambda x: x.upper())
df['State'].unique()

# Only grab where Staus == 1 
mask = df['Status'] == 1 
df = df[mask]

# Convert NJ to NY 
mask = df.State == 'NJ'
df['State'][mask] = 'NY' 

df['State'].unique()

df['CustomerCount'].plot(figsize=(15,5)); 

# If we take a look at the data, we begin to realize that there are multiple values for the same State, StatusDate, and Status combination. It is possible that this means the data you are working with is dirty/bad/inaccurate, but we will assume otherwise. We can assume this data set is a subset of a bigger data set and if we simply add the values in the CustomerCount column per State, StatusDate, and Status we will get the Total Customer Count per day.
sortdf = df[df['State']=='NY'].sort(axis=0)
sortdf.head(10)

# Our task is now to create a new dataframe that compresses the data so we have daily customer counts per State and StatusDate. We can ignore the Status column since all the values in this column are of value 1. To accomplish this we will use the dataframe's functions groupby and sum().
# Note that we had to use reset_index . If we did not, we would not have been able to group by both the State and the StatusDate since the groupby function expects only columns as inputs. The reset_index function will bring the index StatusDate back to a column in the dataframe.

# Group by State and StatusDate
Daily = df.reset_index().groupby(['State','StatusDate']).sum()
Daily.head()


del Daily['Status']
Daily.head()

# What is the index of the dataframe
Daily.index

# Select the State index 
Daily.index.levels[0]

# Select the StatusDate index 
Daily.index.levels[1]

Daily.loc['FL'].plot()
Daily.loc['GA'].plot()
Daily.loc['NY'].plot()
Daily.loc['TX'].plot(); 

Daily.loc['FL']['2012'].plot()
Daily.loc['GA']['2012'].plot()
Daily.loc['NY']['2012'].plot()
Daily.loc['TX']['2012'].plot(); 

# Calculate Outliers 

StateYearMonth = Daily.groupby([Daily.index.get_level_values(0), Daily.index.get_level_values(1).year, Daily.index.get_level_values(1).month])
Daily['Lower'] = StateYearMonth['CustomerCount'].transform( lambda x: x.quantile(q=.25) - (1.5*x.quantile(q=.75)-x.quantile(q=.25)))
Daily['Upper'] = StateYearMonth['CustomerCount'].transform( lambda x: x.quantile(q=.75) + (1.5*x.quantile(q=.75)-x.quantile(q=.25)))
Daily['Outlier'] = (Daily['CustomerCount'] < Daily['Lower']) | (Daily['CustomerCount'] > Daily['Upper'])

# Remove Outliers 
Daily = Daily[Daily['Outlier'] == False]


Daily.head()

# Combine all markets 

# Get the max customer count by Date 
ALL = pd.DataFrame(Daily['CustomerCount'].groupby(Daily.index.get_level_values(1)).sum())
ALL.columns = ['CustomerCount'] # rename column

# Group by Year and Month
YearMonth = ALL.groupby([lambda x: x.year, lambda x: x.month])

# What is the max customer count per Year and Month
ALL['Max'] = YearMonth['CustomerCount'].transform(lambda x: x.max())
ALL.head()

# Create the BHAG (big hairy annual goal) dataframe 

data = [1000,2000,3000]
idx = pd.date_range(start='12/31/2011', end='12/31/2013', freq='A')
BHAG = pd.DataFrame(data, index=idx, columns=['BHAG'])
BHAG

# Combining dataframes as we have learned in previous lesson is made simple using the concat function. Remember when we choose axis = 0 we are appending row wise.

# Combine the BHAG and the ALL data set 
combined = pd.concat([ALL,BHAG], axis=0)
combined = combined.sort(axis=0)
combined.tail()

fig, axes = plt.subplots(figsize=(12, 7))

combined['BHAG'].fillna(method='pad').plot(color='green', label='BHAG')
combined['Max'].plot(color='blue', label='All Markets')
plt.legend(loc='best'); 

# There was also a need to forecast next year's customer count and we can do this in a couple of simple steps. We will first group the combined dataframe by Year and place the maximum customer count for that year. This will give us one row per Year.

# Group by Year and then get the max value per year 
Year = combined.groupby(lambda x: x.year).max()
Year

# Add a column representing the percent change per year 
Year['YR_PCT_Change'] = Year['Max'].pct_change(periods=1)
Year 

# To get next year's end customer count we will assume our current growth rate remains constant. We then will increase this years customer count by that amount and that will be our forecast for next year.
(1 + Year.ix[2012, 'YR_PCT_Change']) * Year.ix[2012, 'Max']

# Create individual graphs per state 

# First Graph 
ALL['Max'].plot(figsize=(10,5));plt.title('ALL Markets')

# Last four graphs 
fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(20,10))
fig.subplots_adjust(hspace=1.0) # Create space between plots 

Daily.loc['FL']['CustomerCount']['2012':].fillna(method='pad').plot(ax=axes[0,0])
Daily.loc['GA']['CustomerCount']['2012':].fillna(method='pad').plot(ax=axes[0,1])
Daily.loc['TX']['CustomerCount']['2012':].fillna(method='pad').plot(ax=axes[1,0])
Daily.loc['NY']['CustomerCount']['2012':].fillna(method='pad').plot(ax=axes[1,1])

# Add titles 
axes[0,0].set_title('Florida')
axes[0,1].set_title('Georgia')
axes[1,0].set_title('Texas')
axes[1,1].set_title('North East'); 





