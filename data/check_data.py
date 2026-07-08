import pandas as pd

# Load data
data = pd.read_csv("building_data.csv")

# Show first rows
print("First 5 rows:")
print(data.head())

# Check null values
print("\nMissing values:")
print(data.isnull().sum())

# Basic statistics
print("\nSummary statistics:")
print(data.describe())

# Correlation
print("\nCorrelation with cost:")
print(data.corr()["cost"].sort_values(ascending=False))

import matplotlib.pyplot as plt

# Scatter plot
plt.scatter(data["area"], data["cost"])
plt.xlabel("Area")
plt.ylabel("Cost")
plt.title("Area vs Cost")
plt.show()