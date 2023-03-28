# Instantiating Main Python Script File
# Collects stuff from the rest of the scripts
import pandas as pd
import numpy as np
import seaborn as sns
import digger
from tkinter.filedialog import askopenfilename

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

import gunner

NA_col_list = [
    "PAL_Sales",
    "JP_Sales",
    "Other_Sales",
    "Global_Sales",
    "User_Score",
    "GameName",
    "Review",
    "",
]
GLO_col_list = [
    "PAL_Sales",
    "JP_Sales",
    "Other_Sales",
    "NA_Sales",
    "User_Score",
    "GameName",
    "Review",
    "",
]
# Collecting Split-Up Datasets
games_sales_split_pre = gunner.game_sales_NA_pre

games_sales_split_dur = gunner.game_sales_NA_dur

games_sales_split_pos = gunner.game_sales_NA_pos

# Displaying Acquired Data
print("Acquired Datasets:\n")
games_sales_split_pre.head(5)
games_sales_split_dur.head(5)
games_sales_split_pos.head(5)

print("Dataset Info:\n")
games_sales_split_pre.info()
games_sales_split_dur.info()
games_sales_split_pos.info()
