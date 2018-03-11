
#import libraries
import pandas as pd
import numpy as np
import pickle
from collections import Counter

#Function to process data that will help in creating labels
def process_data_for_labels(ticker):
    #hm_days: howmanyDays ahead: how many days into the future we want to predict the values
    hm_days = 7
    #Load csv containing the adj closes of all the S&P 500 companies
    df = pd.read_csv('sp500_joined_closes.csv', index_col=0)

    #Tickers: contains names of all the S&P500 companies
    tickers = df.columns.values

    #processing: the data consit of many NAN values: remove it
    df.fillna(0, inplace=True)

    #function to create seven day prediction
    for i in range(1, hm_days+ 1):
        df['{}_{}d'.format(ticker,i)] = (df[ticker].shift(-i) - df[ticker])/df[ticker]

    #processing: the data consit of many NAN values: remove it
    df.fillna(0, inplace=True)

    return tickers, df


#Function that helps in creating a label

def buy_sell_hold(*args):
    #Get the arguments in the list
    cols = [c for c in args]
    #our requirment/decision point
    requirement = 0.02
    for col in cols:
        if col > requirement:
            return 1
        if col < requirement:
            return -1
    return 0

#Function helps in creating features

def extract_featuresets(ticker):
    tickers, df = process_data_for_labels(ticker)
    df['{}_target'.format(ticker)] = list(map(buy_sell_hold, df['{}_1d'.format(ticker)],
                                                             df['{}_2d'.format(ticker)],
                                                             df['{}_3d'.format(ticker)],
                                                             df['{}_4d'.format(ticker)],
                                                             df['{}_5d'.format(ticker)],
                                                             df['{}_6d'.format(ticker)],
                                                             df['{}_7d'.format(ticker)]))


    # print(df['{}_target'.format(ticker)])
    vals = df['{}_target'.format(ticker)].values.tolist()
    str_vals = [str(i) for i in vals]
    # print('Data spread:',Counter(str_vals))

    #Cleaning the data
    df.fillna(0, inplace=True)
    df = df.replace([np.inf, -np.inf], np.nan)
    df.dropna(inplace=True)

    #more important measure pct_change
    df_vals = df[[ticker for ticker in tickers]].pct_change()
    df_vals = df_vals.replace([np.inf, -np.inf], 0)
    df_vals.fillna(0, inplace=True)

    #return featureset X, and target variable y
    X = df_vals.values
    y = df['{}_target'.format(ticker)].values
    print(df_vals.head())
    print(X)
    print(y)
    return X,y,df


extract_featuresets('AAPL')
