# Program to import S&P 500 companies and store in pickle

#import libraries
import bs4 as bs
import pickle
import requests

def save_sp500_tickers():
        tickers = []
        resp = requests.get('https://en.wikipedia.org/wiki/List_of_S%26P_500_companies')
        soup = bs.BeautifulSoup(resp.text, 'html.parser')
        table = soup.find('table' , {'class': 'wikitable sortable'})
        for row in table.findAll('tr')[1:]:
            ticker = row.findAll('td')[0].text
            tickers.append(ticker)

        # store the ticker list into a pickle
        with open("sp500tickers.pickle", "wb") as f:
            pickle.dump(tickers, f)
        print(tickers)
        return tickers

save_sp500_tickers()
