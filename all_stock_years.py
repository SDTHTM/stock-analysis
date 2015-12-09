import pandas as pd
from pandas import DataFrame


import matplotlib.pyplot as plt

pd.options.mode.chained_assignment = None  # default='warn'


#df = pd.read_csv('c:/users/Tina Meredith/data/test2.csv', parse_dates=['date'])
df = pd.read_csv('c:/users/Tina Meredith/data/StockSelections.csv', parse_dates=['date'])

#sort the values according to stock symbol and date
newstock = df[['TSYMBOL','date','PRC']]

#newstock.sort_values(['TSYMBOL','date'],ascending=['TSYMBOL','date'])
newstock.sort(['TSYMBOL','date'],ascending=['TSYMBOL','date'])

symbols = pd.unique(df.TSYMBOL.ravel())

#newstock.plot()

grouped = newstock.groupby('TSYMBOL')

#plottest = grouped.get_group('BAC')

#plottest.plot(x='date', y='PRC')



fig, axes = plt.subplots(nrows=3, ncols=1, figsize=(9,9))


newstock['STD'] = pd.rolling_std(newstock['PRC'],25,min_periods=1)

newstock['KURTOSIS'] = pd.rolling_kurt(newstock['PRC'],25,min_periods=1)
'''
for symbol in symbols:
    plottest = grouped.get_group(symbol)
    plottest.plot(x='date',y='sprtrn',ax=ax,label=symbol)
#    print('here-')
#    print(plottest)
       
#    print(newstock)
'''


for name, group in newstock.groupby('TSYMBOL'):
        #   print(newstock.date)
           #print('here')
           #print(group)
           ax1 = newstock.plot(x='date',y='PRC',kind='line',label=name,title='Stock Prices',ax=axes[0], legend=False) 
           ax2 = newstock.plot(x='date',y='STD',kind='line',label=name,title='Rolling Standard Deviation',ax=axes[1], sharex=ax1, legend=False)
           ax3 = newstock.plot(x='date',y='KURTOSIS',kind='line',label=name,title='Rolling Kurtosis',ax=axes[2],sharex=ax1, legend=False)

plt.tight_layout()                       
plt.legend(loc='best')

plt.show()

#newstock.to_csv('c:/users/Tina Meredith/data/testwrite.csv')
