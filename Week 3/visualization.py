import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

df = sns.load_dataset('titanic')

print("First few rows of the dataset:")
print(df.head())

print("Dataset Info:")
print(df.info())

print("Missing Values:")
print(df.isnull().sum())

df.dropna(subset=['age', 'embarked'], inplace=True)

sns.countplot(x='survived', data=df)
plt.title("Total Survival Count")
plt.show()

sns.countplot(x='sex', hue='survived', data=df)
plt.title("Survival Count by Gender")
plt.show()

sns.countplot(x='class', hue='survived', data=df)
plt.title("Survival Count by Class")
plt.show()

sns.histplot(df['age'], bins=30, kde=True)
plt.title("Age Distribution of Passengers")
plt.xlabel("Age")
plt.show()

sns.scatterplot(x='age', y='fare', hue='survived', data=df)
plt.title("Age vs Fare")
plt.show()
