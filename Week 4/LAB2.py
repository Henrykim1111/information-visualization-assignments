#%% import libraries
import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt
from datetime import datetime
import matplotlib.dates as mdates

pd.set_option('display.float_format', '{:.2f}'.format)

stocks = ['AAPL', 'ORCL', 'TSLA', 'IBM', 'YELP', 'MSFT']
start_date = '2000-01-01'
end_date = '2023-08-28'

#%% Q1

df = yf.download(stocks, start=start_date, end=end_date)['High']
flg, ax=plt.subplots(3,2,
                     figsize = (16,8),
                     )

for i, stock in enumerate(stocks):
    row = int(i / 2)
    col = i % 2
    ax[row, col].plot(df.index, df[stock], label=stock, lw=3)
    ax[row, col].set_title(f'High price history of {stock}', fontsize = 15)
    ax[row, col].set_xlabel('Date', fontsize = 15)
    ax[row, col].set_ylabel('High price USD($)', fontsize = 15)
    ax[row, col].grid(True)
    ax[row, col].legend(loc='upper left', fontsize = 15)

plt.tight_layout()
plt.show()

#%% Q2 - Low


df = yf.download(stocks, start=start_date, end=end_date)['Low']
flg, ax=plt.subplots(3,2,
                     figsize = (16,8),
                     )

for i, stock in enumerate(stocks):
    row = int(i / 2)
    col = i % 2
    ax[row, col].plot(df.index, df[stock], label=stock, lw=3)
    ax[row, col].set_title(f'Low price history of {stock}', fontsize = 15)
    ax[row, col].set_xlabel('Date', fontsize = 15)
    ax[row, col].set_ylabel('Low price USD($)', fontsize = 15)
    ax[row, col].grid(True)
    ax[row, col].legend(loc='upper left', fontsize = 15)

plt.tight_layout()
plt.show()

#%% Q2 - Open


df = yf.download(stocks, start=start_date, end=end_date)['Open']
flg, ax=plt.subplots(3,2,
                     figsize = (16,8),
                     )

for i, stock in enumerate(stocks):
    row = int(i / 2)
    col = i % 2
    ax[row, col].plot(df.index, df[stock], label=stock, lw=3)
    ax[row, col].set_title(f'Open price history of {stock}', fontsize = 15)
    ax[row, col].set_xlabel('Date', fontsize = 15)
    ax[row, col].set_ylabel('Open price USD($)', fontsize = 15)
    ax[row, col].grid(True)
    ax[row, col].legend(loc='upper left', fontsize = 15)

plt.tight_layout()
plt.show()

#%% Q2 - Close


df = yf.download(stocks, start=start_date, end=end_date)['Close']
flg, ax=plt.subplots(3,2,
                     figsize = (16,8),
                     )

for i, stock in enumerate(stocks):
    row = int(i / 2)
    col = i % 2
    ax[row, col].plot(df.index, df[stock], label=stock, lw=3)
    ax[row, col].set_title(f'Close price history of {stock}', fontsize = 15)
    ax[row, col].set_xlabel('Date', fontsize = 15)
    ax[row, col].set_ylabel('Close price USD($)', fontsize = 15)
    ax[row, col].grid(True)
    ax[row, col].legend(loc='upper left', fontsize = 15)

plt.tight_layout()
plt.show()

#%% Q2 - Volume


df = yf.download(stocks, start=start_date, end=end_date)['Volume']
flg, ax=plt.subplots(3,2,
                     figsize = (16,8),
                     )

for i, stock in enumerate(stocks):
    row = int(i / 2)
    col = i % 2
    ax[row, col].plot(df.index, df[stock], label=stock, lw=3)
    ax[row, col].set_title(f'Volume history of {stock}', fontsize = 15)
    ax[row, col].set_xlabel('Date', fontsize = 15)
    ax[row, col].set_ylabel('Volume USD($)', fontsize = 15)
    ax[row, col].grid(True)
    ax[row, col].legend(loc='upper left', fontsize = 15)

plt.tight_layout()
plt.show()

#%% Q2 - Adj Close


df = yf.download(stocks, start=start_date, end=end_date)['Adj Close']
flg, ax=plt.subplots(3,2,
                     figsize = (16,8),
                     )

for i, stock in enumerate(stocks):
    row = int(i / 2)
    col = i % 2
    ax[row, col].plot(df.index, df[stock], label=stock, lw=3)
    ax[row, col].set_title(f'Adj Close price history of {stock}', fontsize = 15)
    ax[row, col].set_xlabel('Date', fontsize = 15)
    ax[row, col].set_ylabel('Adj Close price USD($)', fontsize = 15)
    ax[row, col].grid(True)
    ax[row, col].legend(loc='upper left', fontsize = 15)

plt.tight_layout()
plt.show()

#%% Q3
