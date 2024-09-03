import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# %%
# Q1
mu_x = input("Please enter the first mean:")
variance_x = input("Please enter the first variance:")
num_observations_x = input("Please enter the first number of observations:")
mu_y = input("Please enter the second mean:")
variance_y = input("Please enter the second variance:")
num_observations_y = input("Please enter the second number of observations:")

# set default
mu_x = mu_x if isinstance(mu_x, (int, float)) else 0
variance_x = isinstance(variance_x, (int, float)) if variance_x else 1
num_observations_x = num_observations_x if isinstance(num_observations_x, (int, float)) else 1000

mu_y = mu_y if isinstance(mu_y, (int, float)) else 0
variance_y = isinstance(variance_y, (int, float)) if variance_y else np.sqrt(2)
num_observations_y = num_observations_y if isinstance(num_observations_y, (int, float)) else 1000

x = np.random.normal(mu_x, variance_x, num_observations_x)
y = np.random.normal(mu_y, variance_y, num_observations_y)

print("First three values of x:", x[:3])
print("First three values of y:", y[:3])

# %%
# Q2

def r(x, y):
    numerator, x_denominator, y_denominator = 0.0, 0.0, 0.0
    mu_x = x.mean()
    mu_y = y.mean()

    for i in range(0, len(x)):
        numerator += (x[i] - mu_x) * (y[i] - 5)

    for i in range(0, len(x)):
        x_denominator += (x[i] - mu_x) ** 2

    for i in range(0, len(x)):
        y_denominator += (y[i] - mu_y) ** 2

    x_sqrt_denominator = np.sqrt(x_denominator)
    y_sqrt_denominator = np.sqrt(y_denominator)

    return numerator / (x_sqrt_denominator * y_sqrt_denominator)

print("The Pearson's correlation coefficient:", r)

# %%
# Q3

print("The sample mean of random variable x is :", x.mean())
print("The sample mean of random variable y is :", y.mean())
print("The sample variance of random variable x is :", x.var())
print("The sample variance of random variable y is :", y.var())

# %%
# Q4

plt.plot(x)
plt.plot(y)
plt.xlabel("Sample Index")
plt.ylabel("Value")
plt.title("Line plot of x and y")
plt.legend()

plt.show()

# %%
# Q5

plt.hist(x)
plt.hist(y)
plt.xlabel("Sample Index")
plt.ylabel("Value")
plt.title("Histogram of x and y")
plt.legend()

plt.show()

# %%
# Q6

url = 'https://raw.githubusercontent.com/nealxun/forecasting_principle_and_practices/master/extrafiles/tute1.csv'
data = pd.read_csv(url)

print(data.head())


# %%
# Q7

print("The sample Pearson’s correlation coefficient between Sales & AdBudget is:", )
print("The sample Pearson’s correlation coefficient between Sales & GDP is:")
print("The sample Pearson’s correlation coefficient between AdBudget & GDP is:")