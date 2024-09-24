#%%
import numpy as np
import matplotlib.pyplot as plt

N = 100
x = np.linspace(-10,10,N)
x = np.array(x, dtype=np.complex_)

y1 = x ** 2
y2 = x ** (1/2)

y3 = x ** 3
y4 = x ** (1/3)

fig = plt.figure()

ax1 = fig.add_subplot(2,2,1)
plt.plot(x,y1)
ax1.set_title('$f(x) = x^2$')
ax1.set_xlabel('samples')
ax1.set_ylabel('magnitude')
ax1.grid()

ax2 = fig.add_subplot(2,2,2)
plt.plot(x,y2)
ax2.set_title('$f(x) = \sqrt{x}$')
ax2.set_xlabel('samples')
ax2.set_ylabel('magnitude')
ax2.grid()

ax3 = fig.add_subplot(2,2,3)
plt.plot(x,y3)
ax3.set_title('$f(x) = x^3$')
ax3.set_xlabel('samples')
ax3.set_ylabel('magnitude')
ax3.grid()

ax4 = fig.add_subplot(2,2,4)
plt.plot(x,y4)
ax4.set_title('$f(x) = \sqrt[3]{x}$')
ax4.set_xlabel('samples')
ax4.set_ylabel('magnitude')
ax4.grid()

plt.tight_layout()
plt.show()

#%% Plotting using fig.add_subplot
x = np.linspace(0,10)

y = [10 ** el for el in x]
z = [2 ** el for el in x]

fig = plt.figure(figsize=(10,8))

ax1 = fig.add_subplot(2,2,1)
plt.plot(x,y, color = 'blue', lw=3)
ax1.set_title(r'plot of $10^{x}$')
ax1.set_xlabel('samples')
ax1.set_ylabel('magnitude')
ax1.grid(visible=True, which = 'both', axis = 'both')

ax2 = fig.add_subplot(2,2,2)
plt.plot(x,y, color = 'green', lw=3)
ax2.set_title(r'Log scale plot of $10^{x}$')
ax2.set_xlabel('samples')
ax2.set_ylabel('magnitude')
ax2.set_yscale('log')
ax2.grid(visible=True, which = 'both', axis = 'both')

ax3 = fig.add_subplot(2,2,3)
plt.plot(x,z, color = 'red', lw=3)
ax3.set_title(r'Linear plot of $2^{x}$')
ax3.set_xlabel('samples')
ax3.set_ylabel('magnitude')
ax3.grid(visible=True, which = 'both', axis = 'both')

ax4 = fig.add_subplot(2,2,4)
plt.plot(x,z, color = 'cyan', lw=3)
ax4.set_title('Log scale plot of $2^{x}$')
ax4.set_xlabel('samples')
ax4.set_ylabel('magnitude')
ax4.set_yscale('log')
ax4.grid(visible=True, which = 'both', axis = 'both')

plt.tight_layout()
plt.show()

#%% Plotting using plt.subplots
x = np.linspace(0,10)

y = [10 ** el for el in x]
z = [2 ** el for el in x]

fig, ax = plt.subplots(2,2, figsize = (10,8))


ax[0,0].plot(x,y, color = 'blue', lw=3)
ax[0,0].set_title(r'plot of $10^{x}$')
ax[0,0].set_xlabel('samples')
ax[0,0].set_ylabel('magnitude')
ax[0,0].grid(visible=True, which = 'both', axis = 'both')

ax[0,1].plot(x,y, color = 'green', lw=3)
ax[0,1].set_title(r'Log scale plot of $10^{x}$')
ax[0,1].set_xlabel('samples')
ax[0,1].set_ylabel('magnitude')
ax[0,1].set_yscale('log')
ax[0,1].grid(visible=True, which = 'both', axis = 'both')

ax[1,0].plot(x,z, color = 'red', lw=3)
ax[1,0].set_title(r'Linear plot of $2^{x}$')
ax[1,0].set_xlabel('samples')
ax[1,0].set_ylabel('magnitude')
ax[1,0].grid(visible=True, which = 'both', axis = 'both')

ax[1,1].plot(x,z, color = 'cyan', lw=3)
ax[1,1].set_title('Log scale plot of $2^{x}$')
ax[1,1].set_xlabel('samples')
ax[1,1].set_ylabel('magnitude')
ax[1,1].set_yscale('log')
ax[1,1].grid(visible=True, which = 'both', axis = 'both')

plt.tight_layout()
plt.show()


#%% Reading mnist Dataset

url ="https://raw.githubusercontent.com/rjafari979/Information-Visualization-Data-Analytics-Dataset-/refs/heads/main/mnist_test.csv"
import pandas as pd

df = pd.read_csv(url)
print(df.shape)

#%% plot function

def plot(df, row, col):
    plt.figure()
    for i in range(row*col):
        len_df = df.shape[1] # or len(df)
        pic = df.iloc[i,:].values.reshape(len_df)[1:].reshape(28,28)
        plt.subplot(row,col, i+1)
        plt.imshow(pic)
    plt.tight_layout
    plt.show()

#%% Reading mnist Dataset and plot only the

df_zeros = df[df['label']==0]
row, col = 5, 5
plot(df_zeros, row, col)

plt.tight_layout
plt.show()

#%% Plotting Decision Boundary for four classes

PP = np.array([[1,4],[1,5],[2,4],[2,5],[3,1],[3,2],[4,1],[4,2],[-1,1],[-1,2],[0,1],[0,2],[2,0],[2,-1],[3,0],[3,-1]]).T

figure, ax = plt.subplots(figsize = (8,8))
ax.scatter(PP[0,:4],PP[1,:4],
           color='r',
           label='Group 1',
           marker='^',
           s=200)

ax.scatter(PP[0,4:8],PP[1,4:8],
           color='b',
           label='Group 2',
           marker='o',
           s=200)

ax.scatter(PP[0,8:12],PP[1,8:12],
           color='g',
           label='Group 3',
           marker='s',
           s=200)

ax.scatter(PP[0,12:16],PP[1,12:16],
           color='y',
           label='Group 4',
           marker='*',
           s=200)

w = np.array([[-1.7, 1.4], [2.1,2.5]])
b = np.array([[0.3],[-7.4]])

x = np.linspace(-2, 6, 1000)

y1 = (-w[0, 0] * x - b[0]) / w[0, 1]
y2 = (-w[1, 0] * x - b[1]) / w[1, 1]

ax.plot(x, y1, label='Line 1', color='black', linestyle='--')
ax.plot(x, y2, label='Line 2', color='purple', linestyle='--')

ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.set_xlim([-2, 6])
ax.set_ylim([-3, 6])
ax.legend()
ax.grid(True)

plt.show()