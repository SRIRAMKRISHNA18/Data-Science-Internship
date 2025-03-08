import pandas as pd
import seaborn as sns

# Task 1: Data Cleaning & Missing Value Handling
# Load the Titanic dataset
df = sns.load_dataset("titanic")

# Display initial dataset info
df.info()

# Handle missing values
df.fillna(method='ffill', inplace=True)  # Forward fill as an example

# Remove duplicate entries
df.drop_duplicates(inplace=True)

# Standardize column names
df.columns = df.columns.str.lower().str.replace(' ', '_')

# Display cleaned dataset info
df.info()
