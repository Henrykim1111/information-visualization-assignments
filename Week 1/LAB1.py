import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# %%
# Q1

def get_float_input(prompt, default_float):
    while True:
        user_input = input(prompt)
        try:
            return float(user_input)
        except ValueError:
            print(f"Invalid input. Returning default value: {default_float}")
            return default_float

def get_int_input(prompt, default_int):
    while True:
        user_input = input(prompt)
        try:
            return int(user_input)
        except ValueError:
            print(f"Invalid input. Returning default value: {default_int}")
            return default_int

mu_x = get_float_input("Please enter the first mean:", 0)
variance_x = get_float_input("Please enter the first variance:", 1)
num_observations_x = get_int_input("Please enter the first number of observations:", 1000)
mu_y = get_float_input("Please enter the second mean:", 5)
variance_y = get_float_input("Please enter the second variance:", 2)
num_observations_y = get_int_input("Please enter the second number of observations:", 1000)

while num_observations_x != num_observations_y:
    print("The first number of observations should be the same as the second number of observations")
    num_observations_y = get_int_input("Please enter the second number of observations:", num_observations_y)

x = np.random.normal(mu_x, variance_x, num_observations_x)
y = np.random.normal(mu_y, variance_y, num_observations_y)

print("First three values of x:", x[:3])
print("First three values of y:", y[:3])

# %%
# Q2

def r(x, y):
    mu_x = np.mean(x)
    mu_y = np.mean(y)

    numerator = np.sum((x-mu_x)*(y-5))
    denominator = np.sqrt(np.sum((x-mu_x)**2))*np.sqrt(np.sum((y-mu_y)**2))

    return numerator / denominator

print("The Pearson's correlation coefficient:", r(x, y))

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