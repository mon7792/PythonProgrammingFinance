# programm to combine all the S&P 500 companies Adj_Close column

#Logic
#1. Loop through all the csv File
#2. initialise an empty dataframe and perform a outer join
#3. rename the Adj_Close column to name of the stock
#4 drop the remaiming column

#IMPORT libraries
import bs4 as bs
import pickle
import requests
import datetime as dt
import os
import pandas as pd
import fix_yahoo_finance as yf
import pandas_datareader.data as web
import time
#  Function to get the S&P500 companies names
def save_sp500_tickers():
        tickers = []
        resp = requests.get('https://en.wikipedia.org/wiki/List_of_S%26P_500_companies')
        soup = bs.BeautifulSoup(resp.text, 'html.parser')
        table = soup.find('table' , {'class': 'wikitable sortable'})
        for row in table.findAll('tr')[1:]:
            ticker = row.findAll('td')[0].text
            tickers.append(ticker)

        #Processing the tickers
        tickers = [ tick.replace('.','-').strip() for tick in tickers]
        # store the ticker list into a pickle
        with open("sp500tickers.pickle", "wb") as f:
            pickle.dump(tickers, f)
        print(tickers)
        return tickers

# save_sp500_tickers()

#Function to get the stock data for S&P500 and store the data in a different CSV
#File


def get_data_from_yahoo(reload_sp500=False):
    #get the list of tickers you want to extract the value of the stocks for
    if reload_sp500:
        tickers = save_sp500_tickers()
    else:
        with open("sp500tickers.pickle", "rb") as f:
            tickers = pickle.load(f)

    #check if the directory exists.if not make the directory to store the
    #value
    if not os.path.exists('stocks_dfs'):
        os.makedirs('stocks_dfs')

    #setup for data frame
    start = dt.datetime(2000,1,1)
    end = dt.datetime(2017,12,31)




    # Loop through the tickers
    for ticker in tickers:
        # print('sleep')
        # time.sleep(0.5)
        print(ticker)
        if not os.path.exists('stocks_dfs/{}.csv'.format(ticker)):
            yf.pdr_override()
            df = web.get_data_yahoo (ticker,start, end)
            df.to_csv('stocks_dfs/{}.csv'.format(ticker))
        else:
            print('Already have {}'.format(ticker))

# get_data_from_yahoo()


#Function  to create a compiles dataframe
def compile_data():
    #load the stock name into the tickers list
    with open('sp500tickers.pickle', 'rb') as f:
        tickers = pickle.load(f)

    #initialise an empty dataframe
    main_df = pd.DataFrame()

    #loop through the ticker and load the CSV into a temp dataframe df
    for count,ticker in enumerate(tickers):
        df = pd.read_csv('stocks_dfs/{}.csv'.format(ticker))
        df.set_index('Date', inplace=True)
        df.rename(columns={'Adj Close': ticker}, inplace=True)
        df.drop(['Open','High','Low','Close','Volume'],1, inplace=True)

        if main_df.empty:
            main_df = df
        else:
            main_df = main_df.join(df, how='outer')

        if(count%10 == 0):
            print(count)
    print(main_df.head())
    main_df.to_csv('sp500_joined_closes.csv')

compile_data()
