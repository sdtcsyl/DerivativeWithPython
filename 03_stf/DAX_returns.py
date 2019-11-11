#
# Analyzing DAX Index Quotes and Returns
# Source: http://finance.yahoo.com
# 03_stf/DAX_returns.py
#
# (c) Dr. Yves J. Hilpisch
# Derivatives Analytics with Python
#
from GBM_returns import *

# Read Data for DAX from the Web


def read_dax_data():
    ''' Reads historical DAX data from Yahoo! Finance, calculates log returns,
    realized variance and volatility.'''
    DAX = pd.read_csv('http://hilpisch.com/tr_eikon_eod_data_long.csv',
                      index_col=0, parse_dates=True)['.GDAXI']
    DAX = pd.DataFrame(DAX)
    DAX = DAX.loc['2004-09-30':'2014-09-30']
    DAX.rename(columns={'.GDAXI': 'index'}, inplace=True)
    DAX['returns'] = np.log(DAX['index'] / DAX['index'].shift(1))
    DAX['rea_var'] = 252 * np.cumsum(DAX['returns'] ** 2) / np.arange(len(DAX))
    DAX['rea_vol'] = np.sqrt(DAX['rea_var'])
    DAX = DAX.dropna()
    return DAX


def count_jumps(data, value):
    ''' Counts the number of return jumps as defined in size by value. '''
    jumps = np.sum(np.abs(data['returns']) > value)
    return jumps



if __name__ == "__main__":
    data = read_dax_data()
    
    #the statistics
    print_statistics(data)
    
    # FIGURE 3.6 DAX index level quotes and daily log returns over the period from 01. October 2004 to
    # 30. September 2014
    quotes_returns(data)
    
    # FIGURE 3.7 Histogram of the daily log returns of the DAX over the period from 01. October 2004 to
    # 30. September 2014 (bars) and for comparison the probability density function of the normal
    # distribution with the sample mean and volatility (line)
    return_histogram(data)
    
    # FIGURE 3.8 Quantile-quantile plot of the daily log returns of the DAX over
    # the period from 01. October 2004 to 30. September 2014
    return_qqplot(data)
    
    # FIGURE 3.9 Realized volatility for the DAX over the period from 01. October 2004 to 30.
    # September 2014
    realized_volatility(data)
    
    # FIGURE 3.10 Rolling mean log return (252 days), rolling volatility (252 days) and rolling
    # correlation between both (252 days); dashed lines are averages over the whole period shown
    rolling_statistics(data)
    
    #count_jumps(data, value)