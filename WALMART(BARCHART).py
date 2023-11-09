#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  8 23:15:30 2023

@author: kamalib
"""

#importing libraries
import pandas as pd
import matplotlib.pyplot as plt

#Read file and print
Walmart_Sales= pd.read_csv('/Users/kamalib/Downloads/WALMART_SALES_DATA-1.csv')
print(Walmart_Sales)

#grouping columns together
avg_sales = Walmart_Sales.groupby('Holiday_Flag')['Weekly_Sales'].mean().reset_index()


#Renaming the columns
avg_sales.rename(columns={'Weekly_Sales': 'Average_Sales'}, inplace=True)

#Replacing the columns
avg_sales['Holiday_Flag'] = avg_sales['Holiday_Flag'].replace({0: 'Non-Holiday Week', 1: 'Special Holiday Week'})

#Plot bar chart
plt.bar(x='Holiday_Flag', height='Average_Sales',data=avg_sales)


#To plot xlabel and ylabel
plt.xlabel('Holiday Week')
plt.ylabel('Avg Sales')

#Title to the bar chart
plt.title("Average sale on Non holiday and Special holiday")

#To plot the legend
plt.legend()

#To show the plot
plt.show()


#Inference:
#The chart denotes the comparison of average sales of holiday week and non-holiday week
#It is observed that the average sales of holiday week is more compared to non-holiday week