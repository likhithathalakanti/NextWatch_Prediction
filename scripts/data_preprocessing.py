import pandas as pd

# Load dataset
df = pd.read_csv('data/movies_dataset.csv')

# Basic data preprocessing
df['Release_Date'] = pd.to_datetime(df['Release_Date'])
df = df.dropna(subset=['Title', 'Popularity', 'Vote_Count'])

# Save preprocessed dataset
df.to_csv('data/movies_dataset_cleaned.csv', index=False)

print("Data preprocessing completed. Cleaned dataset saved to 'data/movies_dataset_cleaned.csv'")
