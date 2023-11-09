#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  9 20:05:05 2023

@author: kamalib
"""

#importing libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#Read the file and print
Walmart_Sales= pd.read_csv('/Users/kamalib/Downloads/WALMART_SALES_DATA-1.csv')
print(Walmart_Sales)

##grouping columns together
salesdata = Walmart_Sales.groupby(['Holiday_Flag']).agg({'Weekly_Sales':['sum']})
salesdata[:5]

salesdata1 = Walmart_Sales.groupby(['Holiday_Flag']).agg({'Fuel_Price':['sum']})
salesdata1[:5]

salesdata2 = Walmart_Sales.groupby(['Holiday_Flag']).agg({'Unemployment':['sum']})
salesdata2[:5]

#To plot figure 
plt.figure(figsize = (20,8))

salesdata1[('Fuel_Price', 'sum')].plot()
salesdata2[('Unemployment',  'sum')].plot()


#To plot the legend
plt.legend()

#To show the plot
plt.show()



#Inference
#The orange color line denotes the variation of Unemployment with respect to Holiday Flag
#The blue color line denotes the variation of Unemployment with respect to Holiday Flag