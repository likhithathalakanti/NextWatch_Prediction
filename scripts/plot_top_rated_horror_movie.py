import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load preprocessed dataset
df = pd.read_csv('data/movies_dataset_cleaned.csv')

# Plot 9: Top rated horror movie between 2000 and 2015
plt.figure(figsize=(10, 6))
horror_movies = df[(df['Genre'].str.contains('Horror', na=False)) & (df['Release_Date'].dt.year.between(2000, 2015))]
top_rated_horror = horror_movies.nlargest(1, 'Vote_Average')[['Title', 'Vote_Average']]
sns.barplot(x='Vote_Average', y='Title', data=top_rated_horror, palette='dark')
plt.title('Top Rated Horror Movie (2000-2015)')
plt.xlabel('Vote Average')
plt.ylabel('Movie Title')
plt.savefig('plots/top_rated_horror_movie.png')
plt.close()

print("Plot for top rated horror movie between 2000 and 2015 created and saved as 'top_rated_horror_movie.png'")
