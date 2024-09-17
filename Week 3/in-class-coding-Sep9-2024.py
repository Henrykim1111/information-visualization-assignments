import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from prettytable import PrettyTable
np.random.seed(5764)
np.set_printoptions(precision =  0)
pd.set_option('display.precision', 2)
x = PrettyTable()
x.field_names = ['Index', 'A','B', 'C', 'D']
data = np.random.rand(6,4)
df = pd.DataFrame(data=np.round(data,2), columns=['A','B','C','D'],
                  index = np.arange(1,7))
df = df.reset_index()
for i in range(6):
    x.add_row((df.iloc[i,:]))

print(x.get_string(title = 'Dummy dataset'))


#%%
from pandas_datareader import data
import yfinance as yf
yf.pdr_override()
stocks = ['AAPL','ORCL', 'TSLA', 'IBM','YELP', 'MSFT']
start_date = "2000-01-01"
end_date = "2024-09-10"
df = data.get_data_yahoo(stocks[0], start = start_date,
                         end = end_date)
print(df.tail().to_string())
col = df.columns
plt.figure(figsize=(12,8))
df[col[:-1]].plot()
plt.xlabel('date')
plt.ylabel('USD($)')
plt.grid()
plt.title('Apple stock price')
plt.show()





#%%


mean_x = 1
mean_y = 2
var_x = 1
var_y = 0.1
N = 5000

#%%
x = np.random.normal(mean_x, np.sqrt(var_x), N)
# y = np.random.normal(mean_y, np.sqrt(var_y), N)
y = 2*x + np.random.normal(mean_y, np.sqrt(var_y), N)
plt.figure()
plt.scatter(x,y)
plt.xlabel('x data')
plt.ylabel('y data')
plt.title('scatter plot between x and y')
plt.grid()
plt.tight_layout()
plt.axis('equal')
plt.show()
#%%
X = pd.DataFrame(x)
Y = pd.DataFrame(y)
df = pd.concat([X,Y], axis=1)
print(f'Correlation between x and y '
      f'is {df.corr().iloc[0,1]:.3f}')


#%%
def sk_ew(i,x):
    N = len(x)
    m_i = (1/N)*np.sum((x-np.mean(x))**i)
    return m_i

m3 = sk_ew(3,x)
m2 = sk_ew(2,x)
g1 = m3/m2**(1.5)

print(f'The skewness of x is {g1:.3f}')

plt.figure()
plt.hist(x, bins = 50)
plt.show()
# =====================================
# Non-symmetric synthetic dataset
#=====================================
a = np.array([1,2,3,4,5,100,1000])
plt.figure()
plt.hist(a)
plt.show()



m3 = sk_ew(3,a)
m2 = sk_ew(2,a)
g1 = m3/m2**(1.5)

print(f'The skewness of a is {g1:.3f}')



