import numpy as np
import matplotlib.pyplot as plt

# %%
# Q1
mean, variance = map(float, input("Enter the mean, variance: ").split(", "))
mean = mean if mean else 0

num_observations = int(input("Enter the number of observations: "))

x = np.random.normal(mean, 1, 1000)
y = np.random.normal(5, np.sqrt(2), 1000)

print("First three values of x:", x[:3])
print("First three values of y:", y[:3])

# %%
# Q2
numerator, x_denominator, y_denominator = 0.0, 0.0, 0.0

for i in range(0, len(x)):
    numerator += (x[i]-mean)*(y[i]-5)

for i in range(0, len(x)):
    x_denominator += (x[i]-mean)**2

for i in range(0, len(x)):
    y_denominator += (y[i]-5)**2

x_sqrt_denominator = np.sqrt(x_denominator)
y_sqrt_denominator = np.sqrt(y_denominator)

r = numerator / (x_sqrt_denominator * y_sqrt_denominator)

print("The Pearson's correlation coefficient:", r)

# %%
# Q3

print("The sample mean of random variable x is :", x.mean())
print("The sample mean of random variable y is :", y.mean())
print("The sample variance of random variable x is :", x.var())
print("The sample variance of random variable y is :", y.var())