#
# Analyzing Euribor Interest Rate Data
# Source: http://www.emmi-benchmarks.eu/euribor-org/euribor-rates.html
# 03_stf/EURIBOR_analysis.py
#
# (c) Dr. Yves J. Hilpisch
# Derivatives Analytics with Python
#
import pandas as pd
from GBM_returns import *

# Read Data for Euribor from Excel file


def read_euribor_data():
    ''' Reads historical Euribor data from Excel file, calculates log returns, 
    realized variance and volatility.'''
    EBO = pd.read_excel('EURIBOR_current.xlsx',
                        index_col=0)
    EBO['returns'] = np.log(EBO['1w'] / EBO['1w'].shift(1))
    EBO = EBO.dropna()
    return EBO


# Plot the Term Structure
markers = [',', '-.', '--', '-']


def plot_term_structure(data):
    ''' Plot the term structure of Euribor rates. '''
    plt.figure(figsize=(10, 5))
    for i, mat in enumerate(['1w', '1m', '6m', '12m']):
        plt.plot(data[mat].index, data[mat].values,
                 'b%s' % markers[i], label=mat)
    plt.grid()
    plt.legend()
    plt.xlabel('strike')
    plt.ylabel('implied volatility')
    plt.ylim(0.0, plt.ylim()[1])

if __name__ == "__main__":
    data = read_euribor_data()
        
    # FIGURE 3.13 Histogram of daily log changes in 1 week Euribor in comparison to a normal
    # distribution with same mean and standard deviation (line)
    return_histogram(data)
    
    # FIGURE 3.14 Quantile-quantile plot of the daily log changes in the 1 week Euribor
    return_qqplot(data)
    
    
    rolling_statistics(data)
    
    
    # FIGURE 3.15 Daily quotes of 1 week (dotted), 1 month (dot-dashed), 6 months (dashed) and 1 year
    # Euribor (solid line) over the period from 01. January 1999 to 30. September 2014
    plot_term_structure(data)