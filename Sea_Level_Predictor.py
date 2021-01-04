# -*- coding: utf-8 -*-
"""
Created on Thu Jul 23 19:52:42 2020

@author: HP
"""


import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    x = df['Year']
    y = df['CSIRO Adjusted Sea Level']
    fig, ax = plt.subplots()
    import numpy as np
    plt.scatter(x, y, c=np.sign(y))

    # Create first line of best fit
    slope, intercept, r_value, p_value, stderr = linregress(x, y)
    d1 = pd.Series(list(range(2014, 2050)))
    df1 = pd.DataFrame(d1)
    a = pd.DataFrame(df['Year'].append(df1[0], ignore_index=True))
    a = a.rename(columns={0:'year'})
    a= a['year']
    b = intercept + slope*a
    plt.plot(a, b, 'r', label='fitted line 1')
    plt.legend()
    plt.tight_layout()
    
    # Create second line of best fit
    second = df[df['Year'] >= 2000]
    slope, intercept, r_value, p_value, stderr = linregress(second['Year'], second['CSIRO Adjusted Sea Level'])
    d1 = pd.Series(list(range(2014, 2050)))
    df1 = pd.DataFrame(d1)
    a = pd.DataFrame(df['Year'].append(df1[0], ignore_index=True))
    a = a.rename(columns={0:'year'})
    c = a['year'].iloc[120: ]
    d = intercept + slope*c
    plt.plot(c, d, 'm', label='fitted line 2')
    plt.legend()
    plt.tight_layout()

    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()