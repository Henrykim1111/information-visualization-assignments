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

#%% Histogram Plot
tips[['tip', 'total_bill']].plot(
    kind = 'hist',
    grid = True,
    bins =  50,
    stacked = True,
    title = 'hist plot',
    orientation = 'vertical',
    alpha = 0.5
)
plt.tight_layout()
plt.show()

#%% Pie Chart
explode = (0.01, 0.1, 0.01, 0.01)
tips_group = tips.loc[:,['day', 'total_bill']].groupby('day').sum()
tips_group.plot(
    kind = 'pie',
    y = 'total_bill',
    autopct = '%1.0f%%',
    explode = explode,
)
plt.tight_layout()
plt.show()

#%% gender_in_code
def change(x):
    if x == 'Male':
        return 1
    elif x == 'Female':
        return 2

tips['sex_encoded'] = tips['sex'].apply(change)
print(tips.head())

#%%
tips = sns.load_dataset('tips')

tips['sex_encoded'] = tips['sex'].apply(
    lambda x : 2 if x == 'Female' else 1
)
print(tips.head())

#%% Create a new feature called tip_pct

tips['tip_pct'] = 100 * tips['tip'] / tips['total_bill']
print(tips.head())

#%% Cleaning check
titanic = sns.load_dataset('titanic')
missing_value = titanic.isna().sum()

print(missing_value)

#%% fill the missing age with mean of age
titanic['age'].fillna(titanic['age'].mean(), inplace = True)
titanic['deck'].fillna(titanic['deck'].mode()[0], inplace = True)
missing_value = titanic.isna().sum()

print(missing_value)

#%%
titanic.columns

titanic_male = titanic[titanic['sex']=='male'].count()[0]
titanic_female = titanic[titanic['sex']=='female'].count()[0]

print(f'\nthere are {titanic_male} male on board')
print(f'\nthere are {titanic_female} female on board')