# Cleaning of datasets
# Somewhat main in the beninging

import pandas as pd
import numpy as np

# Sharing the dataset variables
# Games' data
global games_dat
# Sales in NA
global game_sales_NA
# Sales Globally
global game_sales_GLO

# Loading Datasets
game_sales2019_dat = pd.read_csv('datasets/videogames/vgsales-12-4-2019-short.csv')
games_dat = pd.read_csv('datasets/videogames/Games.xls')

# Printing information regarding datasets
print("Data Sets' Info:\n")
game_sales2019_dat.info()
games_dat.info()

# Printing First n values (index start: 0)
print("Game Sale Data:\n", game_sales2019_dat.head(10))
print("Game Scores:\n", games_dat.head(10))

# Regarding the Games.xls dataset:
# Coercing the non-numeric values will result in NaN
# thus allowing easier removal through `.notnull()`
games_dat['Score'] = pd.to_numeric(games_dat['Score'], errors = 'coerce')

games_dat = games_dat[games_dat['Score'].notnull()]

print("Game Scores (Cleaned):\n", games_dat.head())
games_dat.info()

# Regarding the vgsales-12-4-2019 dataset
# Considering we will be using a US (probs CA too) crime datasets
# It wouldn't be that useful to have other columns regarding other regions
NA_col_list = ['PAL_Sales', 'JP_Sales', 'Other_Sales', 'Global_Sales']
GLO_col_list = ['PAL_Sales', 'JP_Sales', 'Other_Sales', 'NA_Sales']

game_sales_NA = game_sales2019_dat.drop(columns = NA_col_list, axis = 1)
game_sales_GLO = game_sales2019_dat.drop(columns = GLO_col_list, axis = 1)

print("Game Sales for NA:\n", game_sales_NA.head(10))
print("Game Sales Globally:\n", game_sales_GLO.head(10))
