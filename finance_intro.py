#PROGRAM: Import data of Tesla Stocks from Yahoo API and Display in the dataframe

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

#dataframe for the data
# DataReader(stock_name,source_of_data,start_date, end_date)
df = web.DataReader('TSLA', 'yahoo', start, end)

#print the dataframe
print(df.head())
