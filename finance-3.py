#PROGRAM: Import data of Tesla Stocks from Yahoo API and plot moving average

#importing libraries
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style
import datetime as dt
import pandas_datareader.data as web

#Setup
#datetime(YYYY,MM,DD)
style.use('ggplot')
start = dt.datetime(2010,6,29)
end = dt.datetime(2018,1,5)

#store data from csv into dataframe
df = pd.read_csv('TSLA.csv', index_col=0, parse_dates=True)

#Add the a new column which shows the moving average
# MOving average takes into consideration the previous values
df['100ma'] = df['Adj Close'].rolling(window=100, min_periods=0).mean()

#print the dataframe

print(df.head())

#plot
#Set the axis for the graph
ax1 = plt.subplot2grid((6,1),(0,0), rowspan=4, colspan=1)
ax2 = plt.subplot2grid((6,1),(4,0), rowspan=2, colspan=1, sharex=ax1)

#plot
ax1.plot(df.index, df['Adj Close'])
ax1.plot(df.index, df['100ma'])

ax2.bar(df.index, df['Volume'])
# df[['High', 'Low']].plot()
plt.show()
