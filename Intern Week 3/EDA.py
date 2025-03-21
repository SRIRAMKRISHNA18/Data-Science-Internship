import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load Dataset (Replace 'your_dataset.csv' with actual filename)
try:
    df = pd.read_csv('C:\Users\srira\OneDrive\Desktop\Intern Week-1\sample_data.csv')
except FileNotFoundError:
    print("Error: The file 'your_dataset.csv' was not found. Please check the file path.")
    exit()

# Check if the dataset is empty
if df.empty:
    print("The dataset is empty. Please provide a valid dataset.")
    exit()

# Display Basic Information
print("Dataset Info:")
df.info()
print("\nSummary Statistics:")
print(df.describe())

# Handling Missing Values (if any)
print("\nMissing Values:")
print(df.isnull().sum())

# Visualizing Data Distribution
plt.figure(figsize=(12, 6))
df.hist(bins=30, figsize=(15, 10), color='skyblue', edgecolor='black')
plt.suptitle('Histograms of Numerical Features')
plt.show()

# Box Plots for Outlier Detection
if not df.select_dtypes(include=['number']).empty:
    plt.figure(figsize=(12, 6))
    sns.boxplot(data=df.select_dtypes(include=['number']))
    plt.xticks(rotation=90)
    plt.title('Boxplot of Numerical Features')
    plt.show()
else:
    print("No numerical features available for boxplot.")

# Correlation Heatmap
if not df.select_dtypes(include=['number']).empty:
    plt.figure(figsize=(10, 6))
    sns.heatmap(df.select_dtypes(include=['number']).corr(), annot=True, cmap='coolwarm', fmt='.2f')
    plt.title('Correlation Heatmap')
    plt.show()
else:
    print("No numerical features available for correlation heatmap.")

# Categorical Data Analysis
categorical_columns = df.select_dtypes(include=['object']).columns
if not categorical_columns.empty:
    for col in categorical_columns:
        plt.figure(figsize=(8, 4))
        sns.countplot(y=df[col], order=df[col].value_counts().index, palette='viridis')
        plt.title(f'Distribution of {col}')
        plt.show()
else:
    print("No categorical features available for analysis.")

print("EDA completed successfully.")