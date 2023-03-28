# Instantiating Main Python Script File
# Collects stuff from the rest of the scripts
import pandas as pd
import numpy as np
import seaborn as sns
import digger
import gunner

# Instantiating globals to be used in other files
global games_merged_dat
global games_sales_split_pre
global games_sales_split_dur
global games_sales_split_pos

games_review = pd.read_csv("datasets/videogames/Games.xls")
games_sales = pd.read_csv("datasets/videogames/vgsales-12-4-2019-short.csv")

games_review_phase1 = digger.slice_column(games_review, "GameName", "Review")
games_review_final = digger.slice_column(games_review, "GameName", "(Import)")

games_merged_dat = digger.write_joined_df(games_sales, games_review_final)

# Acquisition of Merged dataset
games_merged_dat.to_csv("datasets/videogames/games_merged.csv")

# Loading Crime Datasets
crime_CA = pd.read_excel('datasets/crime/clean_crime_canada_dataset.xlsx')

crime_US = pd.read_csv('datasets/crime/report.csv')

year_interval = gunner.year_interval(crime_US, crime_CA, "report_year", "year")

print(year_interval[0], year_interval[1])

crime_intersect = gunner.intersect_by_year(crime_US, crime_CA, "report_year", "year")

NA_col_list = [
    "PAL_Sales",
    "JP_Sales",
    "Other_Sales",
    "Global_Sales",
    "User_Score",
    "GameName",
    "Review",
]
GLO_col_list = [
    "PAL_Sales",
    "JP_Sales",
    "Other_Sales",
    "NA_Sales",
    "User_Score",
    "GameName",
    "Review",
]

# Splitting crime datasets
# Collecting Split-Up Datasets
games_merged_dat = gunner.drop_kick(NA_col_list, games_merged_dat)

sale_tri_split = gunner.trisect_by_year(games_merged_dat, 'Year', year_interval)

# Displaying Acquired Data
print("Acquired Datasets:\n")
print(sale_tri_split[0].head(5),
sale_tri_split[1].head(5),
sale_tri_split[2].head(5))

print("Dataset Info:\n")
sale_tri_split[0].info()
sale_tri_split[1].info()
sale_tri_split[2].info()
