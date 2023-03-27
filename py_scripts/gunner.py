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
# Crime Recorded in The US
global crime_US
# Crime Recorded in Canada
global crime_CA

# Loading Datasets
game_sales_dat = pd.read_csv('datasets/videogames/vgsales-12-4-2019-short.csv')
games_dat = pd.read_csv('datasets/videogames/Games.xls')

crime_CA = pd.read_excel('datasets/crime/clean_crime_canada_dataset.xlsx')
crime_US = pd.read_csv('datasets/crime/report.csv')

# Printing information regarding datasets
print("Game Datasets' Info:\n")
game_sales_dat.info()
games_dat.info()

print("Crime Datasets' Info:\n")
crime_US.info()
crime_CA.info()

# Printing First n values (index start: 0)
print("Game Sale Data:\n", game_sales_dat.head(10))
print("Game Scores:\n", games_dat.head(10))

print("US Crime Data:\n", crime_US.head(10))
print("CA Crime Data:\n", crime_CA.head(10))

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

game_sales_NA = game_sales_dat.drop(columns = NA_col_list, axis = 1)
game_sales_GLO = game_sales_dat.drop(columns = GLO_col_list, axis = 1)

print(f"Game Sales for NA:\n{game_sales_NA.head(10)} \nWith minimum year being: {game_sales_NA['Year'].min()}")
print(f"Game Sales Globally:\n{game_sales_GLO.head(10)}\nWith minimum year being: {game_sales_GLO['Year'].min()}")

# Getting the range of years which both datasets share
crime_year_min = max(crime_US['report_year'].min(), crime_CA['year'].min())
crime_year_max = min(crime_US['report_year'].max(), crime_CA['year'].max())

crime_CA = crime_CA[(crime_CA['year'] >= crime_year_min) & (crime_CA['year'] <= crime_year_max)]
crime_US = crime_US[(crime_US['report_year'] >= crime_year_min) & (crime_US['report_year'] <= crime_year_max)]
