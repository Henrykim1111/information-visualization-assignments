import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

np.random.seed(5764)

#%%
import pandas as pd
url = 'https://raw.githubusercontent.com/rjafari979/Information-Visualization-Data-Analytics-Dataset-/main/tute1.csv'
df = pd.read_csv(url)
print(df.head())


#%%
mean_x = 0
mean_y = mean_x + 5
var_x = 1
N = 1000

x = np.random.normal(mean_x, np.sqrt(var_x), N)
y = np.random.normal(mean_y, np.sqrt(var_x), N)
# print(f'{x[0]:.2f}')

plt.figure()
plt.plot(x, label ='x')
plt.plot(y, label ='y')
plt.legend()
plt.grid()
plt.title(' The x and y R.V')
plt.show()
