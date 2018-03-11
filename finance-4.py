#Program to
#A. Resample data
#B. plot Candlestick graph
# import library
import datetime
import pandas as pd
import matplotlib.pyplot as plt
import pandas_datareader.data as web
from matplotlib import style
# from matplotlib.finance import candlestick_ohlc
import mpl_finance as mp
import matplotlib.dates as mdates

#setup
style.use('ggplot')
ax1 = plt.subplot2grid((6,1), (0,0), rowspan=4, colspan=1)
ax2 = plt.subplot2grid((6,1), (4,0), rowspan=2, colspan=1, sharex=ax1)
ax1.xaxis_date()
# Read csv and store the values in the df
df = pd.read_csv('TSLA.csv', parse_dates=True, index_col=0)

#Resample and Create a Adj Close and Volume dataframe
df_ohlc = df['Adj Close'].resample('10D').ohlc()
df_volume = df['Volume'].resample('10D').sum()
print(df_volume.head())

#convert the dataframe dates to mdates
df_ohlc = df_ohlc.reset_index()
df_ohlc['Date'] = df_ohlc['Date'].map(mdates.date2num)


#display the graph
mp.candlestick_ohlc(ax1, df_ohlc.values, width=2, colorup='g')

#volume graph
ax2.fill_between(df_volume.index.map(mdates.date2num),df_volume.values,0)

plt.show()
