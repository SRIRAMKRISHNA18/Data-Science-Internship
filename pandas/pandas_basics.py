import pandas as pd
# Read the sample CSV file
df = pd.read_csv('sample_data.csv')

# Print the first five rows of the dataset
print("First Five Rows:")
print(df.head())

# Display basic statistics of the dataset
print("\nBasic Statistics:")
print(df.describe())