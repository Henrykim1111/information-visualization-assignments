#%% import libraries
import pandas as pd
from pandas_datareader import data
import yfinance as yf

#%% Q1

stocks = ['AAPL', 'ORCL', 'TSLA', 'IBM', 'YELP', 'MSFT']
start_date = '2013-01-01'
end_date = '2024-05-22'

stock_data = {}
pd.set_option('display.float_format', '{:.2f}'.format)

for stock in stocks:
    stock_data[stock] = yf.download(stock, start=start_date, end=end_date)

for stock in stocks:
    print(stock_data[stock])

#%% Q2
pd.set_option('display.max_columns', None)

columns = ['High ($)', 'Low ($)', 'Open ($)', 'Close ($)', 'Volume', 'Adj Close ($)']
index = stocks + ['Maximum Value', 'Minimum Value', 'Maximum company name', 'Minimum company name']

mean_values = pd.DataFrame(columns=columns, index=index)

for stock in stocks:
    mean_values.loc[stock, 'High ($)'] = stock_data[stock]['High'].mean()
    mean_values.loc[stock, 'Low ($)'] = stock_data[stock]['Low'].mean()
    mean_values.loc[stock, 'Open ($)'] = stock_data[stock]['Open'].mean()
    mean_values.loc[stock, 'Close ($)'] = stock_data[stock]['Close'].mean()
    mean_values.loc[stock, 'Volume'] = stock_data[stock]['Volume'].mean()
    mean_values.loc[stock, 'Adj Close ($)'] = stock_data[stock]['Adj Close'].mean()

for column in columns:
    mean_values.loc['Maximum Value', column] = max(mean_values[column])
    mean_values.loc['Minimum Value', column] = min(mean_values[column])
    mean_values.loc['Maximum company name', column] = max(mean_values[column])
    mean_values.loc['Minimum company name', column] = min(mean_values[column])

print(mean_values)

#%% Q3

var_values = pd.DataFrame(columns=columns, index=index)

for stock in stocks:
    var_values.loc[stock, 'High ($)'] = stock_data[stock]['High'].var()
    var_values.loc[stock, 'Low ($)'] = stock_data[stock]['Low'].var()
    var_values.loc[stock, 'Open ($)'] = stock_data[stock]['Open'].var()
    var_values.loc[stock, 'Close ($)'] = stock_data[stock]['Close'].var()
    var_values.loc[stock, 'Volume'] = stock_data[stock]['Volume'].var()
    var_values.loc[stock, 'Adj Close ($)'] = stock_data[stock]['Adj Close'].var()

for column in columns:
    var_values.loc['Maximum Value', column] = max(var_values[column])
    var_values.loc['Minimum Value', column] = min(var_values[column])
    var_values.loc['Maximum company name', column] = max(var_values[column])
    var_values.loc['Minimum company name', column] = min(var_values[column])

print(var_values)

#%% Q4

std_values = pd.DataFrame(columns=columns, index=index)

# Open High Low Close Adj Close Volume
for stock in stocks:
    std_values.loc[stock, 'High ($)'] = stock_data[stock]['High'].std()
    std_values.loc[stock, 'Low ($)'] = stock_data[stock]['Low'].std()
    std_values.loc[stock, 'Open ($)'] = stock_data[stock]['Open'].std()
    std_values.loc[stock, 'Close ($)'] = stock_data[stock]['Close'].std()
    std_values.loc[stock, 'Volume'] = stock_data[stock]['Volume'].std()
    std_values.loc[stock, 'Adj Close ($)'] = stock_data[stock]['Adj Close'].std()

for column in columns:
    std_values.loc['Maximum Value', column] = max(std_values[column])
    std_values.loc['Minimum Value', column] = min(std_values[column])
    std_values.loc['Maximum company name', column] = max(std_values[column])
    std_values.loc['Minimum company name', column] = min(std_values[column])

print(std_values)

#%% Q5

median_values = pd.DataFrame(columns=columns, index=index)

for stock in stocks:
    median_values.loc[stock, 'High ($)'] = stock_data[stock]['High'].median()
    median_values.loc[stock, 'Low ($)'] = stock_data[stock]['Low'].median()
    median_values.loc[stock, 'Open ($)'] = stock_data[stock]['Open'].median()
    median_values.loc[stock, 'Close ($)'] = stock_data[stock]['Close'].median()
    median_values.loc[stock, 'Volume'] = stock_data[stock]['Volume'].median()
    median_values.loc[stock, 'Adj Close ($)'] = stock_data[stock]['Adj Close'].median()

for column in columns:
    median_values.loc['Maximum Value', column] = max(median_values[column])
    median_values.loc['Minimum Value', column] = min(median_values[column])
    median_values.loc['Maximum company name', column] = max(median_values[column])
    median_values.loc['Minimum company name', column] = min(median_values[column])

print(median_values)

#%% Q6

correlation_aapl = stock_data['AAPL'].corr()

print(correlation_aapl)

#%% Q7

for stock in stocks:
    correlation_stock = stock_data[stock].corr()
    print('correlation of ', stock)
    print(correlation_stock)
    print('\n')

#%% Q8
std_devs = {}

for stock in stocks:
    df = stock_data[stock]
    df['Daily Return'] = df['Adj Close'].pct_change()
    std_devs[stock] = df['Daily Return'].std()

std_dev_df = pd.DataFrame(list(std_devs.items()), columns=['Stock', 'Standard Deviation'])
std_dev_df.sort_values(by=['Stock', 'Standard Deviation'], ascending=True)

print(std_dev_df)

