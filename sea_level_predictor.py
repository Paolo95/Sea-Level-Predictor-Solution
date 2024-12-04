import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import linregress

def draw_plot():
    # Read data from file

    df = pd.read_csv("epa-sea-level.csv")

    # Create scatter plot

    x = df['Year']
    y = df['CSIRO Adjusted Sea Level']

    plt.scatter(x, y, label='Original Data', color='blue')

    # Create first line of best fit

    res = linregress(x, y)
    years_extended = np.arange(x.min(), 2051)
    line_of_best_fit = res.intercept + res.slope * years_extended
    plt.plot(years_extended, line_of_best_fit, 'r', label='Line of Best Fit (through 2050)')

    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')

    # Create second line of best fit
    years_from_2000 = np.arange(2000,2051)
    res = linregress(df[df['Year'] >= 2000]['Year'], df[df['Year'] >= 2000]['CSIRO Adjusted Sea Level'])
    line_of_best_fit_2000 = res.intercept + res.slope * years_from_2000

    # Add labels and title

    plt.plot(years_from_2000, line_of_best_fit_2000, 'g', label='Line of Best Fit (through 2050)')
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()