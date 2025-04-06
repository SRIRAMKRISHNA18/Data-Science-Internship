import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the IPL dataset
df = pd.read_excel(r"C:\Users\srira\OneDrive\Desktop\Intern Week-1\Data-Science-Internship-Basics\Intern Week 4\ipl_stats.xlsx")

# Set Seaborn style
sns.set(style="whitegrid")

# ----- Basic Dataset Info -----
print("Top 5 rows:\n", df.head())
print("\nDataset shape:", df.shape)
print("\nMissing values:\n", df.isnull().sum())
print("\nStatistical Summary:\n", df.describe())

# ----- 1. Top 10 Run Scorers -----
top_runs = df.sort_values(by="Runs", ascending=False).head(10)
plt.figure(figsize=(10, 6))
sns.barplot(x="Runs", y="Player Name", data=top_runs, palette="Greens")
plt.title("Top 10 Run Scorers in IPL")
plt.xlabel("Total Runs")
plt.ylabel("Player Name")
plt.tight_layout()
plt.show()

# ----- 2. Top 10 Wicket Takers -----
top_wickets = df.sort_values(by="Wickets", ascending=False).head(10)
plt.figure(figsize=(10, 6))
sns.barplot(x="Wickets", y="Player Name", data=top_wickets, palette="Reds")
plt.title("Top 10 Wicket Takers in IPL")
plt.xlabel("Total Wickets")
plt.ylabel("Player Name")
plt.tight_layout()
plt.show()

# ----- 3. Team-wise Player Distribution -----
plt.figure(figsize=(10, 6))
sns.countplot(data=df, x="Team", order=df["Team"].value_counts().index, palette="Set2")
plt.title("Number of Players per Team")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# ----- 4. Strike Rate Distribution -----
plt.figure(figsize=(10, 5))
sns.histplot(df["Strike Rate"], kde=True, bins=15, color='purple')
plt.title("Distribution of Strike Rates")
plt.xlabel("Strike Rate")
plt.ylabel("Count")
plt.tight_layout()
plt.show()

# ----- 5. Economy vs Wickets (Bubble Plot) -----
plt.figure(figsize=(10, 6))
sns.scatterplot(data=df, x="Economy", y="Wickets", hue="Team", size="Matches", sizes=(50, 300), palette="deep")
plt.title("Economy vs Wickets (Size ~ Matches)")
plt.xlabel("Economy")
plt.ylabel("Wickets")
plt.tight_layout()
plt.show()
