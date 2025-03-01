import pandas as pd

# Sample data
data = {
    "Name": ["Shriya", "Sriram", "ShriDevi", "Hema", "Akhil", "Surya", "Rishi"],
    "Age": [35, 21, 21, 9, 19, 30, 75],
    "Salary": [90000, 100000, 80000, 100000, 63000, 1500000, 180000],
    "Department": ["HR", "Analyst", "Devloper", "IT", "HR", "Finance", "Analyst"]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Save the DataFrame as a CSV file
df.to_csv("sample_data.csv", index=False)

# Confirm the file has been created
print("sample_data.csv has been created.")