import pandas as pd

dataset = pd.read_csv('scopus.csv')

print("\nFirst 5 rows:")
print(dataset.head())

print("\nLast 5 rows:")
print(dataset.tail())

print("\nDataset shape (rows, columns):")
print(dataset.shape)

print("\nColumn names:")
print(dataset.columns)

print("\nDataset info:")
print(dataset.info())

print("\nStatistical summary (numerical columns):")
print(dataset.describe())

print("\nStatistical summary (all columns):")
print(dataset.describe(include='all'))

# Check missing values
print("\nMissing values in dataset:")
print(dataset.isnull().sum())

# Unique values in each column
print("\nUnique values per column:")
print(dataset.nunique())

# Filter example
print("\nPapers after 2019:")
print(dataset[dataset['Year'] > 2019])

# Grouping example
print("\nAverage citations per field:")
print(dataset.groupby('Field')['Citations'].mean())

# Sort example
print("\nTop cited papers:")
print(dataset.sort_values(by='Citations', ascending=False).head())