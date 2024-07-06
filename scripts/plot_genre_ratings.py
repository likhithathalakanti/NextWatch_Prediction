import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load preprocessed dataset
df = pd.read_csv('data/movies_dataset_cleaned.csv')

# Plot 1: Top genres by average vote
plt.figure(figsize=(10, 6))
top_genres = df.groupby('Genre')['Vote_Average'].mean().sort_values(ascending=False).head(10)
sns.barplot(x=top_genres.values, y=top_genres.index, palette='viridis')
plt.title('Top Genres by Average Vote')
plt.xlabel('Average Vote')
plt.ylabel('Genre')
plt.savefig('plots/top_genres_by_vote.png')
plt.close()

print("Plot for top genres by average vote created and saved as 'top_genres_by_vote.png'")
