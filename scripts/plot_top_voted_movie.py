import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load preprocessed dataset
df = pd.read_csv('data/movies_dataset_cleaned.csv')

# Plot 4: Top voted movie
plt.figure(figsize=(10, 6))
top_voted_movie = df.nlargest(1, 'Vote_Count')[['Title', 'Vote_Count']]
sns.barplot(x='Vote_Count', y='Title', data=top_voted_movie, palette='rocket')
plt.title('Top Voted Movie')
plt.xlabel('Vote Count')
plt.ylabel('Movie Title')
plt.savefig('plots/top_voted_movie.png')
plt.close()

print("Plot for top voted movie created and saved as 'top_voted_movie.png'")
