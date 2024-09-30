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
url = 'https://github.com/rjafari979/Information-Visualization-Data-Analytics-Dataset-/raw/refs/heads/main/Sample%20-%20Superstore.xls'
df = pd.read_excel(url)

plt.figure(figsize=(10,5))
plt.title('Region-wise Revenue', fontsize = 18)

Top_region = df.loc[:,['Quantity', 'Region', 'Sales', 'Discount', 'Profit']].groupby('Region').sum().sort_values('Sales', ascending=False)
Top_region.reset_index(inplace=True)
plt.bar(Top_region['Region'], Top_region['Sales'], color='#FF6F61', label = 'Sales')
plt.bar(Top_region['Region'], Top_region['Quantity'], color='green', edgecolor = 'Red', linewidth = 1, label = 'Quantity')
plt.xlabel("Region", fontsize = 15)
plt.xticks(fontsize = 12, rotation = 45)
plt.yticks(fontsize = 12)
plt.legend()

# Add numerical value of sales to the bar plot
for k,v in Top_region['Sales'].astype('int').items():
    if v > 250000:
        plt.text(k, v - 75000, '$'+str(v), fontsize = 12, color = 'k', horizontalalignment='center')
    else:
        plt.text(k, v - 15000, '$'+str(v), fontsize = 12, color = 'k', horizontalalignment='center')

plt.tight_layout()
plt.show()

#%% 3D Plot
def f(x1, x2):
    return (x1 + x2)**4 - 12*x1*x2 + x1 + x2 + 1

x = np.linspace(-1, 1, 50)
y = np.linspace(-1, 1, 50)
X, Y = np.meshgrid(x, y)
Z = f(X, Y)
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_wireframe(X, Y, Z)
plt.tight_layout()
plt.show()

#%% Contour Plot
plt.figure(figsize=(8,8))
level = np.arange(-3, 5, .5)
CS = plt.contour(X, Y, Z, level, colors ='k')
plt.clabel(CS, inline =1, fontsize = 10)

plt.tight_layout()
plt.title('Simplest default with labels')
plt.axis('equal')
plt.xlim([-1,1])
plt.ylim([-1,1])
plt.show()

#%% Twin Plot
x = np.arange(1,6)
y1 = np.array([10, 15, 7, 12, 9])
y2 = np.array([200, 300, 150, 250, 180])
fig, ax1 = plt.subplots(figsize=(8,4))
ax1.bar(x, y1, color = 'b', alpha = 0.7, label = 'Sales')
ax1.set_xlabel('Month')
ax1.set_ylabel('Sales', color='b')
ax1.set_ylim(0,20)

ax2=ax1.twinx()
ax2.plot(x, y2, color = 'r', marker = 'o', label = 'Revenue')
ax2.set_ylabel('Revenue', color = 'r')
ax2.set_ylim(0,400)
fig.legend(loc='upper left', bbox_to_anchor = (0.15,.85))
plt.title('Sales and Revenue Comparison')
plt.grid(True)
plt.tight_layout()
plt.show()

