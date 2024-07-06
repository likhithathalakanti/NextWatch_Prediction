import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load preprocessed dataset
df = pd.read_csv('data/movies_dataset_cleaned.csv')

# Plot 8: Popularity vs Vote Count for movies released in 2021
plt.figure(figsize=(10, 6))
movies_2021 = df[df['Release_Date'].dt.year == 2021]
sns.scatterplot(x='Vote_Count', y='Popularity', data=movies_2021, hue='Genre', palette='Spectral', s=100)
plt.title('Popularity vs Vote Count (2021 Movies)')
plt.xlabel('Vote Count')
plt.ylabel('Popularity')
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
plt.savefig('plots/popularity_vs_vote_2021.png', bbox_inches='tight')
plt.close()

print("Plot for popularity vs vote count for 2021 movies created and saved as 'popularity_vs_vote_2021.png'")
