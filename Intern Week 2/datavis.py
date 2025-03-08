import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
df_iris = sns.load_dataset("iris")

# Create histograms for numerical columns
df_iris.hist(figsize=(10, 6), bins=20, edgecolor='black')
plt.suptitle("Histograms of Numerical Features in Iris Dataset")
plt.show()

# Create box plots for numerical columns
plt.figure(figsize=(12, 6))
for i, col in enumerate(df_iris.select_dtypes(include=['float64', 'int64']).columns, 1):
    plt.subplot(1, 4, i)
    sns.boxplot(y=df_iris[col])
    plt.title(col)
plt.tight_layout()
plt.show()

# Use Seaborn’s heatmap to visualize correlation
plt.figure(figsize=(8, 6))
sns.heatmap(df_iris.corr(), annot=True, cmap='coolwarm', fmt='.2f')
plt.title("Correlation Heatmap of Iris Dataset")
plt.show()
