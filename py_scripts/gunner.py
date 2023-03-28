# Cleaning of datasets
# Somewhat main in the beninging

import pandas as pd
import numpy as np
import mining_hq

# Sharing the dataset variables
# Games' data

# Loading Datasets
games_merged = mining_hq.games_merged_dat

victim1 = pd.read_excel("datasets/crime/clean_crime_canada_dataset.xlsx")
victim2 = pd.read_csv("datasets/crime/report.csv")

# Printing information regarding datasets
print("Game Datasets' Info:\n")
games_merged.info()

print("Crime Datasets' Info:\n")
victim2.info()
victim1.info()


# Regarding the Games.xls dataset:
# Coercing the non-numeric values will result in NaN
# thus allowing easier removal through `.notnull()`


# Regarding the vgsales-12-4-2019 dataset
# Considering we will be using a US (probs CA too) crime datasets
# It wouldn't be that useful to have other columns regarding other regions
def drop_kick(col_list, dataframe):
    return dataframe.drop(columns=col_list, axis=1)


# Getting the range of years which both datasets share
def year_interval(victim1, victim2, col1, col2):
    return (
        min(victim2[col2].max(), victim1[col1].max()),
        max(victim2[col2].min(), victim1[col1].min()),
    )


def intersect_by_year(victim1, victim2, col1, col2):
    interval = year_interval(victim1, victim2, col1, col2)
    victim1 = victim1[(victim1[col1] >= interval[0]) & (victim1[col1] <= interval[1])]
    victim2 = victim2[(victim2[col2] >= interval[0]) & (victim2[col2] <= interval[1])]
    return (victim1, victim2)


# Updating the NA game dataset to fit with the time ranges
def trisect_by_year(victim1, col, interval):
    victim1_pre = victim1[victim1[col] < interval[0]]
    victim1_dur = victim1[(victim1[col] <= interval[1]) & (victim1[col] >= interval[0])]
    victim1_pos = victim1[victim1[col] > interval[1]]
    return (victim1_pre, victim1_dur, victim1_pos)
