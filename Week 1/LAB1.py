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

x = np.random.normal(mu_x, np.sqrt(variance_x), num_observations_x)
y = np.random.normal(mu_y, np.sqrt(variance_y), num_observations_y)

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

print("The sample mean of random variable x is :", np.mean(x))
print("The sample mean of random variable y is :", np.mean(y))
print("The sample variance of random variable x is :", np.var(x))
print("The sample variance of random variable y is :", np.var(y))

# %%
# Q4

plt.plot(x, label=f'mean : {mu_x}, variance : {variance_x}', color='blue')
plt.plot(y, label=f'mean : {mu_y}, variance : {variance_y}', color='red')
plt.xlabel("Index")
plt.ylabel("Value")
plt.title("Line plot of x and y")
plt.legend()

plt.show()

# %%
# Q5

plt.hist(x, label=f'mean : {mu_x}, variance : {variance_x}', color='blue')
plt.hist(y, label=f'mean : {mu_y}, variance : {variance_y}', color='red')
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.title("Histogram of x and y")
plt.legend()

plt.show()

# %%
# Q6

url = 'https://raw.githubusercontent.com/rjafari979/Information-Visualization-Data-Analytics-Dataset-/main/tute1.csv'
data = pd.read_csv(url)

print(data.head())


# %%
# Q7

print("The sample Pearson’s correlation coefficient between Sales & AdBudget is:", r(data.Sales, data.AdBudget))
print("The sample Pearson’s correlation coefficient between Sales & GDP is:", r(data.GDP, data.Sales))
print("The sample Pearson’s correlation coefficient between AdBudget & GDP is:", r(data.AdBudget, data.GDP))

# %%
# Q8

plt.scatter(data.Sales, data.AdBudget)
plt.title(f"r: {r(data.Sales, data.AdBudget)}")
plt.xlabel("Sales")
plt.ylabel("AdBudget")
plt.grid(True)

plt.show()

# %%
# Q9

plt.scatter(data.Sales, data.GDP)
plt.title(f"r: {r(data.Sales, data.GDP)}")
plt.xlabel("Sales")
plt.ylabel("GDP")
plt.grid(True)

plt.show()

# %%
# Q10

plt.scatter(data.GDP, data.AdBudget)
plt.title(f"r: {r(data.GDP, data.AdBudget)}")
plt.xlabel("GDP")
plt.ylabel("AdBudget")
plt.grid(True)

plt.show()

# %%
# Q11
plt.plot(data.Date, data.Sales, label="Sales", color='red')
plt.plot(data.Date, data.AdBudget, label="AdBudget", color='blue')
plt.plot(data.Date, data.GDP, label="GDP", color='green')
plt.xlabel("Date")
plt.ylabel("Values")
plt.title("Sales, AdBudget, and GDP Over Time")
plt.legend()

plt.xticks(rotation=45, ha='right')

plt.show()

# %%
# Q12

