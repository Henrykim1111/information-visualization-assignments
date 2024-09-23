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