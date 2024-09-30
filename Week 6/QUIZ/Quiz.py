# Q1 : 데이터셋 row, column 개수 구하기
# Q2 : 결측치가 0.2 이상인 컬럼 지우고 콘솔에 띄우기
# Q3 : 수정한 데이터셋이 결측치 없는지 재확인
# Q4 : tip, total의 각각 평균과 분산 구하기
# Q5 : 팁 비율이 0, 10~15, 15~20, 20이상 인 개수 각각 구하기
# Q6 : tip & total 로 히스토그램 그리기
# Q7 : 두 가지 속성 사이에서 코베리언스 구하기



#%% Prior setting
import pandas as pd
import seaborn as sns
pd.set_option('display.float_format', '{:.2f}'.format)

#%% Q1
# Load the 'taxis' dataset from Seaborn package repository.
# How many samples and features are in the raw dataset?
# Display a message on the console and fill out the blank: [6pts]

df = sns.load_dataset('taxis')
print(f"There are {df.shape[0]} observations inside the raw dataset.")
print(f"There are {df.shape[1]} features[columns] inside the raw dataset.")

#%% Q2
for col in df.columns:
    missing_values = df[col].isnull().sum()
    print(missing_values) # payment, #pickup_zone, dropoff_zone, pickup_borough, dropoff_borough

# 6433 * 0.2 * 1/100 = 12.87
# so drop if num of na > 12.87
drop_count = 0
for col in df.columns:
    if df[col].isnull().sum() > (6433 * 0.2 * 1/100):
        df.drop(col, axis=1, inplace=True)
        drop_count += 1


print(f"The cleaned dataset has {df.shape[0]} # of observations.")
print(f"The cleaned dataset has {df.shape[1]} # of features.")
print(f"The list of removed features are {drop_count}")

#%% Q3
print(df.isnull().sum())
print(df.isna().sum())

#%% Q4
print(f"The mean of the total is {round(df['total'].mean(), 2)}$")
print(f"The mean of the tip is {round(df['tip'].mean(), 2)}$")
print(f"The variance of the total is {round(df['total'].var(), 2)}$")
print(f"The variance of the tip is {round(df['tip'].var(), 2)}$")


#%% Q5
df['tip_percentage'] = df['tip'] / df['total']
print(df.tail(n=5))

print("1-", df[df['tip_percentage'] == 0].shape[0])
# print("2-", df[df['tip_percentage'] >= 10 and df[df['tip_percentage'] < 15]].shape[0])
# print("3-", df[df['tip_percentage'] >= 15 and df[df['tip_percentage'] < 20]].shape[0])
print("4-", df[df['tip_percentage'] >= 0.2].shape[0])

#%%