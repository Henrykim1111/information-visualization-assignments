#%% import libraries
import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt
import datetime

pd.set_option('display.float_format', '{:.2f}'.format)

stocks = ['AAPL', 'ORCL', 'TSLA', 'IBM', 'YELP', 'MSFT']

start_date = '2000-01-01'
end_date = '2023-08-28'


#%% Q1

df = yf.download(stocks, start=start_date, end=end_date)['High']
df = df[stocks]


# '2010-06-29'
start_date_tsla = df['TSLA'].first_valid_index()
# '2012-03-02'
start_date_yelp = df['YELP'].first_valid_index()


start_date = pd.to_datetime(start_date)
end_date = pd.to_datetime(end_date)
start_date_tsla = pd.to_datetime(start_date_tsla)
start_date_yelp = pd.to_datetime(start_date_yelp)

ax = df.plot(subplots = True,
             layout = (3,2),
             xlabel = 'Date',
             ylabel = 'High price USD($)',
             figsize = (16,8),
             lw = 3,
             fontsize = 15,
             grid = True,
             legend = True,
             sharex = False,
             color = '#1f77b4'
             )

ax[0,0].set_title('High price history of AAPL', fontsize = 15)
ax[0,0].set_xlim([start_date, end_date])
ax[0,0].legend(loc='upper left', fontsize=15)
ax[0,0].tick_params(axis='x', rotation=0)

ax[0,1].set_title('High price history of ORCL', fontsize = 15)
ax[0,1].set_xlim([start_date, end_date])
ax[0,1].legend(loc='upper left', fontsize=15)
ax[0,1].tick_params(axis='x', rotation=0)

ax[1,0].set_title('High price history of TSLA', fontsize = 15)
ax[1,0].set_xlabel('Date', fontsize = 15)
ax[1,0].set_xlim([start_date_tsla, end_date])
ax[1,0].legend(loc='upper left', fontsize=15)
ax[1,0].tick_params(axis='x', rotation=0)

ax[1,1].set_title('High price history of IBM', fontsize = 15)
ax[1,1].set_xlabel('Date', fontsize = 15)
ax[1,1].set_xlim([start_date, end_date])
ax[1,1].legend(loc='upper left', fontsize=15)
ax[1,1].tick_params(axis='x', rotation=0)

ax[2,0].set_title('High price history of YELP', fontsize = 15)
ax[2,0].set_xlabel('Date', fontsize = 15)
ax[2,0].set_xlim([start_date_yelp, end_date])
ax[2,0].legend(loc='upper left', fontsize=15)
ax[2,0].tick_params(axis='x', rotation=0)

ax[2,1].set_title('High price history of MSFT', fontsize = 15)
ax[2,1].set_xlabel('Date', fontsize = 15)
ax[2,1].set_xlim([start_date, end_date])
ax[2,1].legend(loc='upper left', fontsize=15)
ax[2,1].tick_params(axis='x', rotation=0)

plt.tight_layout()
plt.show()

#%% Q2 - Low


df = yf.download(stocks, start=start_date, end=end_date)['Low']
df = df[stocks]

ax = df.plot(subplots = True,
             layout = (3,2),
             xlabel = 'Date',
             ylabel = 'Low price USD($)',
             figsize = (16,8),
             lw = 3,
             fontsize = 15,
             grid = True,
             legend = True,
             sharex = False,
             color = '#1f77b4'
             )

ax[0,0].set_title('Low price history of AAPL', fontsize = 15)
ax[0,0].set_xlim([start_date, end_date])
ax[0,0].legend(loc='upper left', fontsize=15)
ax[0,0].tick_params(axis='x', rotation=0)

ax[0,1].set_title('Low price history of ORCL', fontsize = 15)
ax[0,1].set_xlim([start_date, end_date])
ax[0,1].legend(loc='upper left', fontsize=15)
ax[0,1].tick_params(axis='x', rotation=0)

ax[1,0].set_title('Low price history of TSLA', fontsize = 15)
ax[1,0].set_xlabel('Date', fontsize = 15)
ax[1,0].set_xlim([start_date_tsla, end_date])
ax[1,0].legend(loc='upper left', fontsize=15)
ax[1,0].tick_params(axis='x', rotation=0)

ax[1,1].set_title('Low price history of IBM', fontsize = 15)
ax[1,1].set_xlabel('Date', fontsize = 15)
ax[1,1].set_xlim([start_date, end_date])
ax[1,1].legend(loc='upper left', fontsize=15)
ax[1,1].tick_params(axis='x', rotation=0)

ax[2,0].set_title('Low price history of YELP', fontsize = 15)
ax[2,0].set_xlabel('Date', fontsize = 15)
ax[2,0].set_xlim([start_date_yelp, end_date])
ax[2,0].legend(loc='upper left', fontsize=15)
ax[2,0].tick_params(axis='x', rotation=0)

ax[2,1].set_title('Low price history of MSFT', fontsize = 15)
ax[2,1].set_xlabel('Date', fontsize = 15)
ax[2,1].set_xlim([start_date, end_date])
ax[2,1].legend(loc='upper left', fontsize=15)
ax[2,1].tick_params(axis='x', rotation=0)

plt.tight_layout()
plt.show()

#%% Q2 - Open


df = yf.download(stocks, start=start_date, end=end_date)['Open']
df = df[stocks]

ax = df.plot(subplots = True,
             layout = (3,2),
             xlabel = 'Date',
             ylabel = 'Open price USD($)',
             figsize = (16,8),
             lw = 3,
             fontsize = 15,
             grid = True,
             legend = True,
             sharex = False,
             color = '#1f77b4'
             )

ax[0,0].set_title('Open price history of AAPL', fontsize = 15)
ax[0,0].set_xlim([start_date, end_date])
ax[0,0].legend(loc='upper left', fontsize=15)
ax[0,0].tick_params(axis='x', rotation=0)

ax[0,1].set_title('Open price history of ORCL', fontsize = 15)
ax[0,1].set_xlim([start_date, end_date])
ax[0,1].legend(loc='upper left', fontsize=15)
ax[0,1].tick_params(axis='x', rotation=0)

ax[1,0].set_title('Open price history of TSLA', fontsize = 15)
ax[1,0].set_xlabel('Date', fontsize = 15)
ax[1,0].set_xlim([start_date_tsla, end_date])
ax[1,0].legend(loc='upper left', fontsize=15)
ax[1,0].tick_params(axis='x', rotation=0)

ax[1,1].set_title('Open price history of IBM', fontsize = 15)
ax[1,1].set_xlabel('Date', fontsize = 15)
ax[1,1].set_xlim([start_date, end_date])
ax[1,1].legend(loc='upper left', fontsize=15)
ax[1,1].tick_params(axis='x', rotation=0)

ax[2,0].set_title('Open price history of YELP', fontsize = 15)
ax[2,0].set_xlabel('Date', fontsize = 15)
ax[2,0].set_xlim([start_date_yelp, end_date])
ax[2,0].legend(loc='upper left', fontsize=15)
ax[2,0].tick_params(axis='x', rotation=0)

ax[2,1].set_title('Open price history of MSFT', fontsize = 15)
ax[2,1].set_xlabel('Date', fontsize = 15)
ax[2,1].set_xlim([start_date, end_date])
ax[2,1].legend(loc='upper left', fontsize=15)
ax[2,1].tick_params(axis='x', rotation=0)

plt.tight_layout()
plt.show()

#%% Q2 - Close


df = yf.download(stocks, start=start_date, end=end_date)['Close']
df = df[stocks]

ax = df.plot(subplots = True,
             layout = (3,2),
             xlabel = 'Date',
             ylabel = 'Close price USD($)',
             figsize = (16,8),
             lw = 3,
             fontsize = 15,
             grid = True,
             legend = True,
             sharex = False,
             color = '#1f77b4'
             )

ax[0,0].set_title('Close price history of AAPL', fontsize = 15)
ax[0,0].set_xlim([start_date, end_date])
ax[0,0].legend(loc='upper left', fontsize=15)
ax[0,0].tick_params(axis='x', rotation=0)

ax[0,1].set_title('Close price history of ORCL', fontsize = 15)
ax[0,1].set_xlim([start_date, end_date])
ax[0,1].legend(loc='upper left', fontsize=15)
ax[0,1].tick_params(axis='x', rotation=0)

ax[1,0].set_title('Close price history of TSLA', fontsize = 15)
ax[1,0].set_xlabel('Date', fontsize = 15)
ax[1,0].set_xlim([start_date_tsla, end_date])
ax[1,0].legend(loc='upper left', fontsize=15)
ax[1,0].tick_params(axis='x', rotation=0)

ax[1,1].set_title('Close price history of IBM', fontsize = 15)
ax[1,1].set_xlabel('Date', fontsize = 15)
ax[1,1].set_xlim([start_date, end_date])
ax[1,1].legend(loc='upper left', fontsize=15)
ax[1,1].tick_params(axis='x', rotation=0)

ax[2,0].set_title('Close price history of YELP', fontsize = 15)
ax[2,0].set_xlabel('Date', fontsize = 15)
ax[2,0].set_xlim([start_date_yelp, end_date])
ax[2,0].legend(loc='upper left', fontsize=15)
ax[2,0].tick_params(axis='x', rotation=0)

ax[2,1].set_title('Close price history of MSFT', fontsize = 15)
ax[2,1].set_xlabel('Date', fontsize = 15)
ax[2,1].set_xlim([start_date, end_date])
ax[2,1].legend(loc='upper left', fontsize=15)
ax[2,1].tick_params(axis='x', rotation=0)

plt.tight_layout()
plt.show()

#%% Q2 - Volume


df = yf.download(stocks, start=start_date, end=end_date)['Volume']
df = df[stocks]

ax = df.plot(subplots = True,
             layout = (3,2),
             xlabel = 'Date',
             ylabel = 'Volume price USD($)',
             figsize = (16,8),
             lw = 3,
             fontsize = 15,
             grid = True,
             legend = True,
             sharex = False,
             color = '#1f77b4'
             )

ax[0,0].set_title('Volume price history of AAPL', fontsize = 15)
ax[0,0].set_xlim([start_date, end_date])
ax[0,0].legend(loc='upper left', fontsize=15)
ax[0,0].tick_params(axis='x', rotation=0)

ax[0,1].set_title('Volume price history of ORCL', fontsize = 15)
ax[0,1].set_xlim([start_date, end_date])
ax[0,1].legend(loc='upper left', fontsize=15)
ax[0,1].tick_params(axis='x', rotation=0)

ax[1,0].set_title('Volume price history of TSLA', fontsize = 15)
ax[1,0].set_xlabel('Date', fontsize = 15)
ax[1,0].set_xlim([start_date_tsla, end_date])
ax[1,0].legend(loc='upper left', fontsize=15)
ax[1,0].tick_params(axis='x', rotation=0)

ax[1,1].set_title('Volume price history of IBM', fontsize = 15)
ax[1,1].set_xlabel('Date', fontsize = 15)
ax[1,1].set_xlim([start_date, end_date])
ax[1,1].legend(loc='upper left', fontsize=15)
ax[1,1].tick_params(axis='x', rotation=0)

ax[2,0].set_title('Volume price history of YELP', fontsize = 15)
ax[2,0].set_xlabel('Date', fontsize = 15)
ax[2,0].set_xlim([start_date_yelp, end_date])
ax[2,0].legend(loc='upper left', fontsize=15)
ax[2,0].tick_params(axis='x', rotation=0)

ax[2,1].set_title('Volume price history of MSFT', fontsize = 15)
ax[2,1].set_xlabel('Date', fontsize = 15)
ax[2,1].set_xlim([start_date, end_date])
ax[2,1].legend(loc='upper left', fontsize=15)
ax[2,1].tick_params(axis='x', rotation=0)

plt.tight_layout()
plt.show()

#%% Q2 - Adj Close


df = yf.download(stocks, start=start_date, end=end_date)['Adj Close']
df = df[stocks]

ax = df.plot(subplots = True,
             layout = (3,2),
             xlabel = 'Date',
             ylabel = 'Adj Close price USD($)',
             figsize = (16,8),
             lw = 3,
             fontsize = 15,
             grid = True,
             legend = True,
             sharex = False,
             color = '#1f77b4'
             )

ax[0,0].set_title('Adj Close price history of AAPL', fontsize = 15)
ax[0,0].set_xlim([start_date, end_date])
ax[0,0].legend(loc='upper left', fontsize=15)
ax[0,0].tick_params(axis='x', rotation=0)

ax[0,1].set_title('Adj Close price history of ORCL', fontsize = 15)
ax[0,1].set_xlim([start_date, end_date])
ax[0,1].legend(loc='upper left', fontsize=15)
ax[0,1].tick_params(axis='x', rotation=0)

ax[1,0].set_title('Adj Close price history of TSLA', fontsize = 15)
ax[1,0].set_xlabel('Date', fontsize = 15)
ax[1,0].set_xlim([start_date_tsla, end_date])
ax[1,0].legend(loc='upper left', fontsize=15)
ax[1,0].tick_params(axis='x', rotation=0)

ax[1,1].set_title('Adj Close price history of IBM', fontsize = 15)
ax[1,1].set_xlabel('Date', fontsize = 15)
ax[1,1].set_xlim([start_date, end_date])
ax[1,1].legend(loc='upper left', fontsize=15)
ax[1,1].tick_params(axis='x', rotation=0)

ax[2,0].set_title('Adj Close price history of YELP', fontsize = 15)
ax[2,0].set_xlabel('Date', fontsize = 15)
ax[2,0].set_xlim([start_date_yelp, end_date])
ax[2,0].legend(loc='upper left', fontsize=15)
ax[2,0].tick_params(axis='x', rotation=0)

ax[2,1].set_title('Adj Close price history of MSFT', fontsize = 15)
ax[2,1].set_xlabel('Date', fontsize = 15)
ax[2,1].set_xlim([start_date, end_date])
ax[2,1].legend(loc='upper left', fontsize=15)
ax[2,1].tick_params(axis='x', rotation=0)

plt.tight_layout()
plt.show()

#%% Q3

df = yf.download(stocks, start=start_date, end=end_date)['High']
df = df[stocks]

ax = df.plot(subplots = True,
             kind = 'hist',
             bins=50,
             layout = (3,2),
             xlabel = 'Value in USD($)',
             ylabel = 'Frequency',
             figsize = (16,8),
             lw = 3,
             fontsize = 15,
             grid = True,
             legend = True,
             sharex=False,
             color = '#1f77b4'
             )

ax[0,0].set_title('High price history of AAPL', fontsize = 15)
ax[0,0].legend(loc='upper right', fontsize=15)
ax[0,0].tick_params(axis='x', rotation=0)

ax[0,1].set_title('High price history of ORCL', fontsize = 15)
ax[0,1].legend(loc='upper right', fontsize=15)
ax[0,1].tick_params(axis='x', rotation=0)

ax[1,0].set_title('High price history of TSLA', fontsize = 15)
ax[1,0].legend(loc='upper right', fontsize=15)
ax[1,0].tick_params(axis='x', rotation=0)

ax[1,1].set_title('High price history of IBM', fontsize = 15)
ax[1,1].legend(loc='upper right', fontsize=15)
ax[1,1].tick_params(axis='x', rotation=0)

ax[2,0].set_title('High price history of YELP', fontsize = 15)
ax[2,0].legend(loc='upper right', fontsize=15)
ax[2,0].tick_params(axis='x', rotation=0)

ax[2,1].set_title('High price history of MSFT', fontsize = 15)
ax[2,1].legend(loc='upper right', fontsize=15)
ax[2,1].tick_params(axis='x', rotation=0)

plt.tight_layout()
plt.show()

#%% Q4 - Low

df = yf.download(stocks, start=start_date, end=end_date)['Low']
df = df[stocks]

ax = df.plot(subplots = True,
             kind = 'hist',
             bins=50,
             layout = (3,2),
             sharex=False,
             xlabel = 'Value in USD($)',
             ylabel = 'Frequency',
             figsize = (16,8),
             lw = 3,
             fontsize = 15,
             grid = True,
             legend = True,
             color = '#1f77b4'
             )

ax[0,0].set_title('Low price history of AAPL', fontsize = 15)
ax[0,0].legend(loc='upper right', fontsize=15)
ax[0,0].tick_params(axis='x', rotation=0)

ax[0,1].set_title('Low price history of ORCL', fontsize = 15)
ax[0,1].legend(loc='upper right', fontsize=15)
ax[0,1].tick_params(axis='x', rotation=0)

ax[1,0].set_title('Low price history of TSLA', fontsize = 15)
ax[1,0].legend(loc='upper right', fontsize=15)
ax[1,0].tick_params(axis='x', rotation=0)

ax[1,1].set_title('Low price history of IBM', fontsize = 15)
ax[1,1].legend(loc='upper right', fontsize=15)
ax[1,1].tick_params(axis='x', rotation=0)

ax[2,0].set_title('Low price history of YELP', fontsize = 15)
ax[2,0].legend(loc='upper right', fontsize=15)
ax[2,0].tick_params(axis='x', rotation=0)

ax[2,1].set_title('Low price history of MSFT', fontsize = 15)
ax[2,1].legend(loc='upper right', fontsize=15)
ax[2,1].tick_params(axis='x', rotation=0)

plt.tight_layout()
plt.show()

#%% Q4 - Open

df = yf.download(stocks, start=start_date, end=end_date)['Open']
df = df[stocks]

ax = df.plot(subplots = True,
             kind = 'hist',
             bins=50,
             layout = (3,2),
             sharex=False,
             xlabel = 'Value in USD($)',
             ylabel = 'Frequency',
             figsize = (16,8),
             lw = 3,
             fontsize = 15,
             grid = True,
             legend = True,
             color = '#1f77b4'
             )

ax[0,0].set_title('Open price history of AAPL', fontsize = 15)
ax[0,0].legend(loc='upper right', fontsize=15)
ax[0,0].tick_params(axis='x', rotation=0)

ax[0,1].set_title('Open price history of ORCL', fontsize = 15)
ax[0,1].legend(loc='upper right', fontsize=15)
ax[0,1].tick_params(axis='x', rotation=0)

ax[1,0].set_title('Open price history of TSLA', fontsize = 15)
ax[1,0].legend(loc='upper right', fontsize=15)
ax[1,0].tick_params(axis='x', rotation=0)

ax[1,1].set_title('Open price history of IBM', fontsize = 15)
ax[1,1].legend(loc='upper right', fontsize=15)
ax[1,1].tick_params(axis='x', rotation=0)

ax[2,0].set_title('Open price history of YELP', fontsize = 15)
ax[2,0].legend(loc='upper right', fontsize=15)
ax[2,0].tick_params(axis='x', rotation=0)

ax[2,1].set_title('Open price history of MSFT', fontsize = 15)
ax[2,1].legend(loc='upper right', fontsize=15)
ax[2,1].tick_params(axis='x', rotation=0)

plt.tight_layout()
plt.show()

#%% Q4 - Close

df = yf.download(stocks, start=start_date, end=end_date)['Close']
df = df[stocks]

ax = df.plot(subplots = True,
             kind = 'hist',
             bins=50,
             layout = (3,2),
             sharex=False,
             xlabel = 'Value in USD($)',
             ylabel = 'Frequency',
             figsize = (16,8),
             lw = 3,
             fontsize = 15,
             grid = True,
             legend = True,
             color = '#1f77b4'
             )

ax[0,0].set_title('Close price history of AAPL', fontsize = 15)
ax[0,0].legend(loc='upper right', fontsize=15)
ax[0,0].tick_params(axis='x', rotation=0)

ax[0,1].set_title('Close price history of ORCL', fontsize = 15)
ax[0,1].legend(loc='upper right', fontsize=15)
ax[0,1].tick_params(axis='x', rotation=0)

ax[1,0].set_title('Close price history of TSLA', fontsize = 15)
ax[1,0].legend(loc='upper right', fontsize=15)
ax[1,0].tick_params(axis='x', rotation=0)

ax[1,1].set_title('Close price history of IBM', fontsize = 15)
ax[1,1].legend(loc='upper right', fontsize=15)
ax[1,1].tick_params(axis='x', rotation=0)

ax[2,0].set_title('Close price history of YELP', fontsize = 15)
ax[2,0].legend(loc='upper right', fontsize=15)
ax[2,0].tick_params(axis='x', rotation=0)

ax[2,1].set_title('Close price history of MSFT', fontsize = 15)
ax[2,1].legend(loc='upper right', fontsize=15)
ax[2,1].tick_params(axis='x', rotation=0)

plt.tight_layout()
plt.show()

#%% Q4 - Volume


df = yf.download(stocks, start=start_date, end=end_date)['Volume']
df = df[stocks]

ax = df.plot(subplots = True,
             kind = 'hist',
             bins=50,
             layout = (3,2),
             sharex=False,
             xlabel = 'Value in USD($)',
             ylabel = 'Frequency',
             figsize = (16,8),
             lw = 3,
             fontsize = 15,
             grid = True,
             legend = True,
             color = '#1f77b4'
             )

ax[0,0].set_title('Volume price history of AAPL', fontsize = 15)
ax[0,0].legend(loc='upper right', fontsize=15)
ax[0,0].tick_params(axis='x', rotation=0)

ax[0,1].set_title('Volume price history of ORCL', fontsize = 15)
ax[0,1].legend(loc='upper right', fontsize=15)
ax[0,1].tick_params(axis='x', rotation=0)

ax[1,0].set_title('Volume price history of TSLA', fontsize = 15)
ax[1,0].legend(loc='upper right', fontsize=15)
ax[1,0].tick_params(axis='x', rotation=0)

ax[1,1].set_title('Volume price history of IBM', fontsize = 15)
ax[1,1].legend(loc='upper right', fontsize=15)
ax[1,1].tick_params(axis='x', rotation=0)

ax[2,0].set_title('Volume price history of YELP', fontsize = 15)
ax[2,0].legend(loc='upper right', fontsize=15)
ax[2,0].tick_params(axis='x', rotation=0)

ax[2,1].set_title('Volume price history of MSFT', fontsize = 15)
ax[2,1].legend(loc='upper right', fontsize=15)
ax[2,1].tick_params(axis='x', rotation=0)

plt.tight_layout()
plt.show()

#%% Q4 - Adj Close


df = yf.download(stocks, start=start_date, end=end_date)['Adj Close']
df = df[stocks]

ax = df.plot(subplots = True,
             kind = 'hist',
             bins=50,
             layout = (3,2),
             sharex=False,
             xlabel = 'Value in USD($)',
             ylabel = 'Frequency',
             figsize = (16,8),
             lw = 3,
             fontsize = 15,
             grid = True,
             legend = True,
             color = '#1f77b4'
             )

ax[0,0].set_title('Adj Close price history of AAPL', fontsize = 15)
ax[0,0].legend(loc='upper right', fontsize=15)
ax[0,0].tick_params(axis='x', rotation=0)

ax[0,1].set_title('Adj Close price history of ORCL', fontsize = 15)
ax[0,1].legend(loc='upper right', fontsize=15)
ax[0,1].tick_params(axis='x', rotation=0)

ax[1,0].set_title('Adj Close price history of TSLA', fontsize = 15)
ax[1,0].legend(loc='upper right', fontsize=15)
ax[1,0].tick_params(axis='x', rotation=0)

ax[1,1].set_title('Adj Close price history of IBM', fontsize = 15)
ax[1,1].legend(loc='upper right', fontsize=15)
ax[1,1].tick_params(axis='x', rotation=0)

ax[2,0].set_title('Adj Close price history of YELP', fontsize = 15)
ax[2,0].legend(loc='upper right', fontsize=15)
ax[2,0].tick_params(axis='x', rotation=0)

ax[2,1].set_title('Adj Close price history of MSFT', fontsize = 15)
ax[2,1].legend(loc='upper right', fontsize=15)
ax[2,1].tick_params(axis='x', rotation=0)

plt.tight_layout()
plt.show()

#%% Q5

df = yf.download('AAPL', start=start_date, end=end_date)

features = df[['High', 'Low', 'Open', 'Close', 'Volume', 'Adj Close']]

pd.plotting.scatter_matrix(features,
                           hist_kwds={'bins': 50},
                           alpha=0.5,
                           s=10,
                           diagonal='kde',
                           figsize=(10,10)
                           )
plt.suptitle('Scatter Matrix of AAPL Stock Features', fontsize=15)

plt.tight_layout()
plt.show()

#%% Q6 - ORCL

df = yf.download('ORCL', start=start_date, end=end_date)

features = df[['High', 'Low', 'Open', 'Close', 'Volume', 'Adj Close']]

pd.plotting.scatter_matrix(features,
                           hist_kwds={'bins': 50},
                           alpha=0.5,
                           s=10,
                           diagonal='kde',
                           figsize=(10,10)
                           )

plt.suptitle('Scatter Matrix of ORCL Stock Features', fontsize=15)


plt.tight_layout()
plt.show()

#%% Q6 - TSLA

df = yf.download('TSLA', start=start_date, end=end_date)

features = df[['High', 'Low', 'Open', 'Close', 'Volume', 'Adj Close']]

pd.plotting.scatter_matrix(features,
                           hist_kwds={'bins': 50},
                           alpha=0.5,
                           s=10,
                           diagonal='kde',
                           figsize=(10,10)
                           )

plt.suptitle('Scatter Matrix of TSLA Stock Features', fontsize=15)


plt.tight_layout()
plt.show()

#%% Q6 - IBM

df = yf.download('IBM', start=start_date, end=end_date)

features = df[['High', 'Low', 'Open', 'Close', 'Volume', 'Adj Close']]

pd.plotting.scatter_matrix(features,
                           hist_kwds={'bins': 50},
                           alpha=0.5,
                           s=10,
                           diagonal='kde',
                           figsize=(10,10)
                           )

plt.suptitle('Scatter Matrix of IBM Stock Features', fontsize=15)


plt.tight_layout()
plt.show()

#%% Q6 - YELP

df = yf.download('YELP', start=start_date, end=end_date)

features = df[['High', 'Low', 'Open', 'Close', 'Volume', 'Adj Close']]

pd.plotting.scatter_matrix(features,
                           hist_kwds={'bins': 50},
                           alpha=0.5,
                           s=10,
                           diagonal='kde',
                           figsize=(10,10)
                           )

plt.suptitle('Scatter Matrix of YELP Stock Features', fontsize=15)


plt.tight_layout()
plt.show()

#%% Q6 - MSFT

df = yf.download('MSFT', start=start_date, end=end_date)

features = df[['High', 'Low', 'Open', 'Close', 'Volume', 'Adj Close']]

pd.plotting.scatter_matrix(features,
                           hist_kwds={'bins': 50},
                           alpha=0.5,
                           s=10,
                           diagonal='kde',
                           figsize=(10,10)
                           )

plt.suptitle('Scatter Matrix of MSFT Stock Features', fontsize=15)


plt.tight_layout()
plt.show()

