import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns

tmdb = pd.read_csv('ml-latest-small\\tmdb_5000_movies.csv')
print(tmdb.head())