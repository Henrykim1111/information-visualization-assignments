#%%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#%%
data = pd.Series([1,2,3,4],
                 index=['a','b','c','d'])
print(data.describe())
print(data)

#%% Bar plot
data1 = pd.Series({'a':10, 'b':20, 'c':30, 'd':40})
print(data1)
data1.plot(kind = 'bar')
plt.show()

#%% Horizontal Bar plot
data1.plot(kind = 'barh')
plt.show()

#%% Box plot
data1.plot(kind = 'box')
plt.show()

#%% KDE plot
data1.plot(kind = 'kde')
plt.show()

#%% Area plot
data1.plot(kind = 'area')
plt.show()

#%% 2D dataframe
np.random.seed(5764) # Course number
data2 = np.random.rand(6,4)
index_nme = ['one', 'two', 'three', 'four', 'five', 'six']
df = pd.DataFrame(data=data2,
                  columns=['A','B','C','D'],
                  index = index_nme)
print(df)

#%% Method 2
data_List = [
    ['Alic', 25, 'Engineer'],
    ['Bob', 30, 'Data scientist'],
    ['Charlie', 28, 'Designer']
]
columns = ['Name', 'Age', 'Occupation']
df = pd.DataFrame(data = data_List,
                  columns = columns)

print(df)

#%%
data_3 = np.random.rand(10,4)
df = pd.DataFrame(data = data_3,
                  columns = ['A', 'B', 'C', 'D'])
plt.figure()
ax = df.plot(subplots = True,
             layout = (4,1),
             xlabel = 'x-axis',
             ylabel = 'y-axis',
             xlim = (0,8),
             ylim = (0,2),
             figsize = (8,8),
             lw = 3,
             grid = True,
             title = 'dummy dataset',
             style = ['b*-', 'ro-', 'y^-', 'cD-'])
ax[0,0].set_ylabel('Mag.1', fontsize = 15)
ax[1,0].set_ylabel('Mag.2', fontsize = 15)
ax[2,0].set_ylabel('Mag.3', fontsize = 15)
ax[3,0].set_ylabel('Mag.4', fontsize = 15)
ax[0,0].set_xlabel('Samples', fontsize = 15)
ax[0,0].set_title('dummy dataset', fontsize = 15)
plt.tight_layout()
plt.show()

#%% seaborn
import seaborn as sns
tips = sns.load_dataset('tips')
date = pd.date_range(start = '1-1-2000',
                     periods=len(tips),
                     freq='D')
tips.index = date
plt.figure()
tips[['total_bill', 'tip']].plot(
    kind = 'line',
    title = 'tip datasert',
    xlabel = 'time',
    ylabel = 'USD',
    grid = True,
    fontsize = 10,

)
plt.show()

#%% Groupy aggregation on Tip dataset
tips_group = tips.loc[:, ['day', 'total_bill']].groupby('day').sum()
tips_group = tips_group.reset_index()
tips_group = tips_group.sort_values(by='total_bill',
                                    ascending=True)

print(tips_group)
plt.figure()

tips_group.plot(kind = 'bar',
                x = 'day',
                y = 'total_bill',
                title = 'bar plot',
                xlabel = 'day',
                ylabel = 'USD($)',
                grid=True,
                fontsize = 10,)

plt.tight_layout()
plt.show()