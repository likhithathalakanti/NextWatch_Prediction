import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load preprocessed dataset
df = pd.read_csv('data/movies_dataset_cleaned.csv')

# Plot 5: Most voted English language movie
plt.figure(figsize=(10, 6))
english_movies = df[df['Original_Language'] == 'en']
top_voted_english_movie = english_movies.nlargest(1, 'Vote_Count')[['Title', 'Vote_Count']]
sns.barplot(x='Vote_Count', y='Title', data=top_voted_english_movie, palette='icefire')
plt.title('Top Voted English Language Movie')
plt.xlabel('Vote Count')
plt.ylabel('Movie Title')
plt.savefig('plots/top_voted_english_movie.png')
plt.close()

print("Plot for top voted English language movie created and saved as 'top_voted_english_movie.png'")
