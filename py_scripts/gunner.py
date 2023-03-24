# Cleaning of datasets
# Somewhat main in the beninging

import pandas as pd
import numpy as np

# Loading Datasets
game_sales2019_dat = pd.read_csv('datasets/videogames/vgsales-12-4-2019-short.csv')
games_dat = pd.read_csv('datasets/videogames/Games.xls')

# Printing information regarding datasets
game_sales2019_dat.info()
games_dat.info()

# Printing First n values (index start: 0)
print(game_sales2019_dat.head(10))
print(games_dat.head(10))

# Coercing the non-numeric values will result in NaN
# thus allowing easier removal through `.notnull()`
games_dat['Score'] = pd.to_numeric(games_dat['Score'], errors = 'coerce')

games_dat = games_dat[games_dat['Score'].notnull()]

games_dat.info()
print(games_dat.head())
