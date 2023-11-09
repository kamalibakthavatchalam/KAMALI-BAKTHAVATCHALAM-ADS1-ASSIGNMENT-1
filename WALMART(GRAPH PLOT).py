#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  8 23:18:09 2023

@author: kamalib
"""

#importing libraries
import pandas as pd
import matplotlib.pyplot as plt

#Read the file and print
df_Walmart_Sales= pd.read_csv('/Users/kamalib/Downloads/WALMART_SALES_DATA-1.csv')
print(df_Walmart_Sales)

#grouping fuel_price together
shop = df_Walmart_Sales.groupby(['Store']).agg({'Fuel_Price':['mean','max','sum']})
shop[:5]

#grouping  Unemployment
shop2 = df_Walmart_Sales.groupby(['Store']).agg({'Unemployment':['sum']})

#To plot the figure
plt.figure(figsize = (20,8))

#Plot the two shop with labels
plt.plot(shop[('Fuel_Price',  'sum')])
plt.plot(shop2[('Unemployment', 'sum')])


#To plot xlabel and ylabel
plt.xlabel('Store')
plt.ylabel('Factors')
  

#Tittle to the line graph
plt.title("Fuel vs unemployment")


#To plot the legend
plt.legend()


#To show the plot
plt.show()




#Inference:
#The chart denotes the comparison of stores with various factors
#The factors taken into consideration are Fuel price and Unemployment