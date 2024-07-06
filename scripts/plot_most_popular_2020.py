import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load preprocessed dataset
df = pd.read_csv('data/movies_dataset_cleaned.csv')

# Plot 7: Most popular movie in 2020
plt.figure(figsize=(10, 6))
movies_2020 = df[df['Release_Date'].dt.year == 2020]
most_popular_2020 = movies_2020.nlargest(1, 'Popularity')[['Title', 'Popularity']]
sns.barplot(x='Popularity', y='Title', data=most_popular_2020, palette='cubehelix')
plt.title('Most Popular Movie in 2020')
plt.xlabel('Popularity')
plt.ylabel('Movie Title
