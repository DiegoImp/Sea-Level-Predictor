import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import numpy as np


def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv', index_col='Year')

    # Create scatter plot
    fig = plt.figure(figsize=(10, 10))
    ax1 = fig.add_subplot(1, 1, 1)
    ax1.scatter(df.index, df['CSIRO Adjusted Sea Level'], c='b', label='Data')

    # Create first line of best fit
    BestFit1 = linregress(df.index, df['CSIRO Adjusted Sea Level'])

    # Generate a range of years till 2050
    years_extended = np.arange(df.index.min(), 2051)
    ax1.plot(years_extended, BestFit1.intercept + BestFit1.slope *
             years_extended, 'g', label='Best Fit Line 1')

    # Create second line of best fit
    BestFit2 = linregress(df.loc[2000:].index,
                          df.loc[2000:]['CSIRO Adjusted Sea Level'])
    years_2000_onwards = np.arange(2000, 2051)
    ax1.plot(years_2000_onwards, BestFit2.intercept +
             BestFit2.slope*years_2000_onwards, 'r', linewidth=2)

    # Add labels and title
    ax1.set_xlabel('Year')
    ax1.set_ylabel('Sea Level (inches)')
    ax1.set_title('Rise in Sea Level')

    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()
