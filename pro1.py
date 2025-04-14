import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

# Load the data
file = r"C:\Users\gande\OneDrive\Desktop\vcard-personal-portfolio-master\A-1_NO_OF_VILLAGES_TOWNS_HOUSEHOLDS_POPULATION_AND_AREA-_1_.csv"
data = pd.read_csv(file, skiprows=1)

# Rename columns
data.columns = [
    "state", "district", "subdist", "type", "name", "area_type",
    "inhab", "uninhab", "towns", "houses", "totalpop", "malepop",
    "femalepop", "area", "popdens"
]

# Clean numeric data
cols = ["inhab", "uninhab", "towns", "houses", "totalpop", "malepop", "femalepop", "area", "popdens"]
for c in cols:
    data[c] = pd.to_numeric(data[c].astype(str).str.replace(",", ""), errors="coerce")

data.fillna(0, inplace=True)

# Calculate derived metrics
data["area"] = data["area"].replace(0, np.nan)
data["real_density"] = data["totalpop"] / data["area"]
data["real_density"] = data["real_density"].replace([np.inf, -np.inf], np.nan).fillna(0)

data["sexratio"] = (data["femalepop"] / data["malepop"]) * 1000
data["avg_house"] = data["totalpop"] / data["houses"]
data["inhab_pct"] = (data["inhab"] / (data["inhab"] + data["uninhab"])) * 100

# Summary stats
print(data.describe())
print("Mean:\n", data.mean(numeric_only=True))
print("Mode:\n", data.mode(numeric_only=True).iloc[0])
print("Median:\n", data.median(numeric_only=True))

# Heatmap
plt.figure(figsize=(12, 6))
sns.heatmap(data[cols + ["sexratio", "real_density"]].corr(), annot=True, cmap="coolwarm")
plt.title("Heatmap of All Numbers")
plt.tight_layout()
plt.show()

# Histogram of total population
plt.figure(figsize=(10, 5))
sns.histplot(data["totalpop"], bins=30, kde=True, color='orange')
plt.title("Total Population Distribution")
plt.xlabel("Total Population")
plt.ylabel("Count")
plt.tight_layout()
plt.show()

# Top 10 regions by sex ratio (bar plot with reduced bar width)
top_sex = data.sort_values("sexratio", ascending=False).drop_duplicates("name").head(10)
plt.figure(figsize=(12, 6))
sns.barplot(data=top_sex, x="name", y="sexratio", hue="name", dodge=False, legend=False, width=0.3)
plt.xticks(rotation=90)
plt.title("Top 10 Regions by Sex Ratio")
plt.ylabel("Ratio")
plt.tight_layout()
plt.show()

# Top 10 regions by number of houses (pie chart instead of bar plot)
top_house = data.sort_values("houses", ascending=False).drop_duplicates("name").head(10)
plt.figure(figsize=(8, 8))
plt.pie(top_house["houses"], labels=top_house["name"], autopct='%1.1f%%', startangle=140)
plt.title("Top 10 Regions by Number of Houses")
plt.tight_layout()
plt.show()

# Scatter plot: Area vs Total Population
plt.figure(figsize=(10, 6))
sns.scatterplot(data=data, x="area", y="totalpop")
plt.title("Area vs Total Population")
plt.xlabel("Area")
plt.ylabel("Population")
plt.tight_layout()
plt.show()

# Histogram: Real Density
plt.figure(figsize=(10, 6))
sns.histplot(data["real_density"], bins=30, kde=True, color='blue')
plt.title("Distribution of Population Density")
plt.xlabel("Density")
plt.ylabel("Count")
plt.tight_layout()
plt.show()

# Fixed Boxplot: Real Density
plt.figure(figsize=(6, 8))
sns.boxplot(y=data["real_density"], color="violet")
plt.title("Population Density Boxplot")
plt.ylabel("Density")
plt.tight_layout()
plt.show()

# Histogram: Inhabited Area Percentage
plt.figure(figsize=(10, 5))
sns.histplot(data["inhab_pct"], bins=20, color="green", kde=True)
plt.title("Inhabited Area Percentage")
plt.xlabel("Percentage")
plt.ylabel("Count")
plt.tight_layout()
plt.show()

# Z-score Outlier detection
z = np.abs(stats.zscore(data[cols]))
outs = (z > 3).any(axis=1)
print("Total outliers:", outs.sum())

# T-test between male and female population
t, p = stats.ttest_ind(data["malepop"], data["femalepop"])
print("T-test between males and females")
print("T:", t)
print("P:", p)

# Export cleaned data
data.to_csv("cleaned_village_data_final.csv", index=False)
