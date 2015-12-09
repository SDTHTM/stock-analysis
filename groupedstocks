#import modules and formulas
import csv
import numpy as np
import pandas as pd
from pandas import DataFrame
from scipy.stats import skew
from scipy.stats import kurtosis


#using pandas to import csv, format date field and set location of file
df = pd.read_csv('F:/Working/StockSelections.csv', parse_dates=['date'])

#creating table of needed columns only
newstock = df[['TICKER','date','PRC']]

#sorting column
newstock.sort(['TICKER','date'],ascending=['TICKER','date'])

#create a grouping by the stock's name
grouped = newstock.groupby('TICKER')

#calculates values for stocks
a=grouped.aggregate([np.mean, np.median, np.min, np.max, np.ptp, np.std, np.var, skew, kurtosis])

#produced written results for the stock's values 
print a 
