#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  8 23:18:59 2023

@author: kamalib
"""

#importing libraries
import pandas as pd
import matplotlib.pyplot as plt


#Read file and print
df_Walmart_Sales= pd.read_csv('/Users/kamalib/Downloads/WALMART_SALES_DATA-1.csv')
df_Walmart_Sales.head()
df_Walmart_Sales.shape


#Extracting the columns and print
df_Walmart_Sales.isnull().sum()
df_Walmart_Sales.info()
 
#To set the date according to month & year
df_Walmart_Sales['Month'] = pd.DatetimeIndex(df_Walmart_Sales['Date']).month
df_Walmart_Sales['Year'] = pd.DatetimeIndex(df_Walmart_Sales['Date']).year
df_Walmart_Sales.head()


#To calculate the sales usings counts
Holiday = df_Walmart_Sales['Holiday_Flag'].value_counts().index
Holiday_Count = df_Walmart_Sales['Holiday_Flag'].value_counts().values

#To plot the pie chart
plt.pie(Holiday_Count,labels=['Holiday','Non-Holiday'])

#Title to the pie chart
plt.title("holiday&non-holiday")

#To plot the legend
plt.legend(loc=1)


#To show the plot
plt.show()



#Inference:
#The pie chart denotes the count of purchase on holidays and non-holidays
#The purchase on holidays is more than non-holidays.