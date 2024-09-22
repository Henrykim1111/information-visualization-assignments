#%% import libraries
import pandas as pd
import yfinance as yf
pd.set_option('display.float_format', '{:.2f}'.format)

stocks = ['AAPL', 'ORCL', 'TSLA', 'IBM', 'YELP', 'MSFT']
start_date = '2000-01-01'
end_date = '2023-08-28'

#%% Q1
