# Instantiating Main Python Script File
# Collects stuff from the rest of the scripts
import pandas as pd
import scout
import numpy as np
import seaborn as sns
import digger, gunner

# Instantiating globals to be used in other files
global games_merged_dat
global games_sales_split_pre
global games_sales_split_dur
global games_sales_split_pos

games_review = pd.read_csv("datasets/videogames/Games.xls")
games_sales = pd.read_csv("datasets/videogames/vgsales-12-4-2019-short.csv")

print(games_review.count())
print(games_sales.count())

games_review_phase1 = digger.slice_column(games_review, "GameName", "Review")
games_review_final = digger.slice_column(games_review, "GameName", "(Import)")

games_merged_dat = digger.write_joined_df(games_sales, games_review_final)

# Acquisition of Merged dataset
print(games_merged_dat.count())

# Loading Crime Datasets
crime_CA = pd.read_excel("datasets/crime/clean_crime_canada_dataset.xlsx")

crime_US = pd.read_csv("datasets/crime/report.csv")

print(crime_US.isnull())
print(crime_CA.isnull())

year_interval = gunner.year_interval(crime_US, crime_CA, "report_year", "year")

year_max = year_interval[0]
year_min = year_interval[1]

crime_intersect = gunner.intersect_by_year(crime_US, crime_CA, "report_year", "year")

crime_US_intersect = crime_intersect[0]
crime_CA_intersect = crime_intersect[1]

NA_col_list = [
    "PAL_Sales",
    "JP_Sales",
    "Other_Sales",
    "Global_Sales",
    "GameName",
    "Review",
    "Console",
    "Score",
]
GLO_col_list = [
    "PAL_Sales",
    "JP_Sales",
    "Other_Sales",
    "NA_Sales",
    "GameName",
    "Review",
    "Console",
    "Score",
]

# Splitting crime datasets
# Collecting Split-Up Datasets
games_merged_dat = gunner.drop_kick(NA_col_list, games_merged_dat)
games_merged_dat.to_csv("datasets/videogames/games_merged.csv", index=False)

sale_tri_split = gunner.trisect_by_year(games_merged_dat, "Year", year_interval)

games_sales_split_pre = sale_tri_split[0]
games_sales_split_dur = sale_tri_split[1]
games_sales_split_pos = sale_tri_split[2]

# Displaying Acquired Data
print("Acquired Datasets:\n")
print(sale_tri_split[0].head(5), sale_tri_split[1].head(5), sale_tri_split[2].head(5))

print("Dataset Info:\n")
sale_tri_split[0].info()
sale_tri_split[1].info()
sale_tri_split[2].info()


print("Dataset Info:\n")
games_sales_split_pre.info()
games_sales_split_dur.info()
games_sales_split_pos.info()

print("Yer forsaken Statistical Description:\n", games_sales_split_dur.describe())

print(
    games_sales_split_pre.head(5),
    games_sales_split_dur.head(5),
    games_sales_split_pos.head(5),
)
# Required to use binning for cleaning, idk
# https://towardsdatascience.com/data-preprocessing-with-python-pandas-part-5-binning-c5bd5fd1b950

# Also need to transform using Z-score (normal distr go brrrr lmao), or min-max

# Need similarity and dissimialrity, scipy time

# Load merged gammas

gammas = pd.read_csv("datasets/videogames/games_merged.csv")
labels = ["smol", "epik", "larg"]
gammas = digger.slam_dunk(gammas, "Critic_Score", labels=labels)
# gammas = gammas[gammas["Genre"].isna() == False]
# gammas = scout.cure_depression(gammas)
gammas.to_csv("output.csv", index=False)
