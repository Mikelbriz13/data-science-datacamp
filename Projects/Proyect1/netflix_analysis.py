# Importing pandas and matplotlib
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Read in the Netflix CSV as a DataFrame
netflix_df = pd.read_csv("netflix_data.csv")

# Start coding here! Use as many cells as you like
duration = 0
for lab, row in netflix_df.iterrows():
    
    duration = duration + netflix_df['duration'][lab]

duration = duration / lab
duration = int(duration)
print(duration)

# Short action movies

netflix_act = netflix_df[netflix_df['genre'] == 'Action']

short_movies = netflix_act[netflix_act['duration'] < 90]

netflix_act_mov = short_movies[short_movies['type'] == 'Movie']

netflix_act_mov_90 = netflix_act_mov[np.logical_and(netflix_act_mov['release_year'] >= 1990,netflix_act_mov['release_year'] <= 1999)]
short_movie_count = len(netflix_act_mov_90)
print(short_movie_count)
