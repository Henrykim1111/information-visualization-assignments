import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 2*np.pi, 100)
y = np.sin(x)

plt.plot(x,y, label = 'sine curve', lw = 3, color = 'red')
plt.fill_between(x, y>0.75, alpha=0.4, color = 'blue')
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.grid(True)
plt.legend()
plt.show()
#%%
font1 = {'family':'serif', 'color':'blue', 'size':20}
font2 = {'family':'serif', 'color':'darkred', 'size':15}

y1 = np.sin(x)
y2 = np.cos(x)

plt.figure(figsize=(8,6))
plt.plot(x,y1, '--', label = 'sine wave', color = 'blue', lw= 3)
plt.plot(x, y2, '--', label = 'cosine wave', color = 'red', lw= 3)
plt.fill_between(x, y1, y2, where = (y1 > y2), alpha = 0.3, color = 'green')
plt.fill_between(x, y1, y2, where = (y1 < y2), alpha = 0.3, color = 'orange')
plt.annotate('area where sine is greater that''cosine', fontsize = 13, xy=(2,0.25), xytext=(3,1), arrowprops=dict(facecolor = 'green', color = 'green', arrowstyle = '->'))

plt.xlabel('x-axis', fontdict=font2)
plt.xlabel('y-axis', fontdict=font2)
plt.legend(prop={'size':15})
plt.title('Fill between x and y', fontdict=font1)
plt.grid(True)
plt.show()

#%%
import pandas as pd
df = pd.read_excel('Sample - Superstore.xls')
print(df.head())