import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load preprocessed dataset
df = pd.read_csv('data/movies_dataset_cleaned.csv')

# Plot 3: Most popular languages
plt.figure(figsize=(10, 6))
top_languages = df.groupby('Original_Language')['Popularity'].sum().sort_values(ascending=False).head(10)
sns.barplot(x=top_languages.values, y=top_languages.index, palette='cividis')
plt.title('Top 10 Most Popular Languages')
plt.xlabel('Total Popularity')
plt.ylabel('Language')
plt.savefig('plots/top_10_popular_languages.png')
plt.close()

print("Plot for top 10 most popular languages created and saved as 'top_10_popular_languages.png'")
