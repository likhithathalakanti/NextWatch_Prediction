
## Dataset
The dataset used is the "9000 Movies Dataset" from Kaggle. It contains the following columns:
- Release Date
- Title
- Overview
- Popularity
- Vote Count
- Vote Average
- Original Language
- Genre
- Poster URL

## Usage
1. **Preprocess the Data**:
   - Run the `data_preprocessing.py` script to preprocess the dataset.
     ```bash
     python scripts/data_preprocessing.py
     ```

2. **Generate Visualizations**:
   - Run the individual plot scripts to generate the corresponding plots. The plots will be saved in the `plots/` directory.
     ```bash
     python scripts/plot_genre_ratings.py
     python scripts/plot_most_popular_movie.py
     python scripts/plot_language_popularity.py
     python scripts/plot_top_voted_movie.py
     python scripts/plot_top_voted_english_movie.py
     python scripts/plot_top_voted_action_movie.py
     python scripts/plot_most_popular_2020.py
     python scripts/plot_popularity_vs_vote_2021.py
     python scripts/plot_top_rated_horror_movie.py
     python scripts/plot_most_popular_2015_2016.py
     ```

## Visualizations
1. **Top Genres by Average Vote**:
   - File: `top_genres_by_vote.png`
   - Description: Bar plot showing the top genres based on average vote.

2. **Most Popular Movies**:
   - File: `top_10_most_popular_movies.png`
   - Description: Bar plot showing the top 10 most popular movies.

3. **Most Popular Languages**:
   - File: `top_10_popular_languages.png`
   - Description: Bar plot showing the top 10 most popular languages based on movie popularity.

4. **Top Voted Movie**:
   - File: `top_voted_movie.png`
   - Description: Bar plot showing the movie with the highest vote count.

5. **Top Voted English Language Movie**:
   - File: `top_voted_english_movie.png`
   - Description: Bar plot showing the English language movie with the highest vote count.

6. **Top Voted Action Movie in English Language**:
   - File: `top_voted_action_movie.png`
   - Description: Bar plot showing the highest vote count for action genre movies in English language.

7. **Most Popular Movie in 2020**:
   - File: `most_popular_2020.png`
   - Description: Bar plot showing the most popular movie in the year 2020.

8. **Popularity vs Vote Count (2021 Movies)**:
   - File: `popularity_vs_vote_2021.png`
   - Description: Scatter plot showing the relationship between popularity and vote count for movies released in 2021.

9. **Top Rated Horror Movie (2000-2015)**:
   - File: `top_rated_horror_movie.png`
   - Description: Bar plot showing the top-rated horror movie between the years 2000 and 2015.

10. **Most Popular Movie (2015-2016)**:
    - File: `most_popular_2015_2016.png`
    - Description: Bar plot showing the most popular movie between the years 2015 and 2016.
