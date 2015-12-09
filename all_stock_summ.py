import pandas as pd
from pandas import DataFrame

import datetime

import pandas.io.data
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import skew
from scipy.stats import kurtosis


df = pd.read_csv('c:/data/StockSelections.csv', parse_dates=['date'])

df['ABSPRC'] = abs(df.PRC)

df['SPREAD_CALC'] = df.ASKHI - df.BIDLO
 

#only keep stock symbol and date
newstock = df[['TSYMBOL','date','ABSPRC']]


grouped = newstock.groupby('TSYMBOL')

chartstock = grouped['ABSPRC'].agg([np.min, np.mean, np.std])
#print(grouped['PRC'].agg([np.min, np.mean, np.std]))

#ax1 = chartstock.subplot(kind='barh')

fig, axes = plt.subplots(nrows=2, ncols=1, figsize=(9,9))
#df1.plot(ax=axes[0,0])
#df2.plot(ax=axes[0,1])

chartstock.plot(kind='bar', title='Stock Prices for 2004-2014',ax=axes[0])


#now plot based on returns
returnstock = df[['TSYMBOL','SPREAD_CALC']]

groupedreturn = returnstock.groupby('TSYMBOL')

chartreturns = groupedreturn['SPREAD_CALC'].agg([np.min, np.mean, np.max])

#print(chartreturns)

#ax2 = chartreturns.subplot(kind='barh',shareax=ax1)
chartreturns.plot(kind='bar',title='Stock Return Spread',ax=axes[1])

plt.tight_layout()

plt.show()

#newstock['STD'] = pd.rolling_std(newstock['PRC'],25,min_periods=1)
