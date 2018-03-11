#PROGRAM: Import data of Tesla Stocks from Yahoo API and Store into csv

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

#function to write api data to csv file
#dataframe for the data
# DataReader(stock_name,source_of_data,start_date, end_date)
def initial_load():
    df = web.DataReader('TSLA', 'yahoo', start, end)
    df.to_csv('TSLA.csv')

#store data from csv into dataframe
df = pd.read_csv('TSLA.csv', index_col=0, parse_dates=True)
#print the dataframe
print(df.head())


#plot
df[['High', 'Low']].plot()
plt.show()
