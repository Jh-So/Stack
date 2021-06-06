import yfinance as yf
import pandas as pd


TickerList = pd.read_csv('./Input/TickerList.csv', encoding = 'cp949', index_col='num')

for i in range(len(TickerList.index)):

    ticker = TickerList.iloc[i]
    ticker = ticker[0] #series type을 문자열로 변경

    # get stock info
    hist = yf.download(ticker)

    filename = '%s.csv'%ticker
    hist.to_csv('./Output/NYSE/%s'%filename, index = True, encoding = 'cp949')

