import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load preprocessed dataset
df = pd.read_csv('data/movies_dataset_cleaned.csv')

# Plot 2: Most popular movies
plt.figure(figsize=(10, 6))
top_movies = df.nlargest(10, 'Popularity')[['Title', 'Popularity']]
sns.barplot(x='Popularity', y='Title', data=top_movies, palette='magma')
plt.title('Top 10 Most Popular Movies')
plt.xlabel('Popularity')
plt.ylabel('Movie Title')
plt.savefig('plots/top_10_most_popular_movies.png')
plt.close()

print("Plot for top 10 most popular movies created and saved as 'top_10_most_popular_movies.png'")
