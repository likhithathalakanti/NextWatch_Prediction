import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load preprocessed dataset
df = pd.read_csv('data/movies_dataset_cleaned.csv')

# Plot 10: Most popular movie between 2015 and 2016
plt.figure(figsize=(10, 6))
movies_2015_2016 = df[df['Release_Date'].dt.year.isin([2015, 2016])]
most_popular_2015_2016 = movies_2015_2016.nlargest(1, 'Popularity')[['Title', 'Popularity']]
sns.barplot(x='Popularity', y='Title', data=most_popular_2015_2016, palette='twilight')
plt.title('Most Popular Movie (2015-2016)')
plt.xlabel('Popularity')
plt.ylabel('Movie Title')
plt.savefig('plots/most_popular_2015_2016.png')
plt.close()

print("Plot for most popular movie between 2015 and 2016 created and saved as 'most_popular_2015_2016.png'")
