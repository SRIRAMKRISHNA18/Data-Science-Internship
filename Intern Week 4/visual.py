# 1. Load the Data
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load a sample dataset (Iris from seaborn, or replace with pd.read_csv('your_dataset.csv'))
df = sns.load_dataset('iris')  # Replace with: df = pd.read_csv("your_dataset.csv")

# 2. Basic Analysis
print("First 5 rows of the dataset:")
print(df.head())

print("\nShape of the dataset:")
print(f"Rows: {df.shape[0]}, Columns: {df.shape[1]}")

print("\nColumn names and data types:")
print(df.dtypes)

# 3. Data Summary
print("\nSummary statistics:")
print(df.describe())

print("\nChecking for missing values:")
print(df.isnull().sum())

# 4. Visualization

# Bar chart: Count of each species
plt.figure(figsize=(6, 4))
sns.countplot(x='species', data=df)
plt.title('Count of each Species')
plt.show()

# Line plot: Sepal length across samples
plt.figure(figsize=(10, 4))
plt.plot(df['sepal_length'], label='Sepal Length')
plt.title('Sepal Length Across Samples')
plt.xlabel('Sample Index')
plt.ylabel('Sepal Length (cm)')
plt.legend()
plt.show()

# Scatter plot: Sepal vs Petal length
plt.figure(figsize=(6, 5))
sns.scatterplot(data=df, x='sepal_length', y='petal_length', hue='species')
plt.title('Sepal Length vs Petal Length')
plt.show()
