import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load preprocessed dataset
df = pd.read_csv('data/movies_dataset_cleaned.csv')

# Plot 6: Highest vote count for action genre in English language
plt.figure(figsize=(10, 6))
action_english_movies = df[(df['Original_Language'] == 'en') & (df['Genre'].str.contains('Action', na=False))]
top_voted_action_movie = action_english_movies.nlargest(1, 'Vote_Count')[['Title', 'Vote_Count']]
sns.barplot(x='Vote_Count', y='Title', data=top_voted_action_movie, palette='inferno')
plt.title('Top Voted Action Movie in English Language')
plt.xlabel('Vote Count')
plt.ylabel('Movie Title')
plt.savefig('plots/top_voted_action_movie.png')
plt.close()

print("Plot for top voted action movie in English language created and saved as 'top_voted_action_movie.png'")
