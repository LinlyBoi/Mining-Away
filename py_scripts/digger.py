# Getting and combining data
import pandas as pd
import numpy as np

global games_merged_dat

# reading the data
# -> MAKE SURE OF THE DATA FRAMES NAMES PEFORE YOU RUN IT

games_dat = pd.read_csv("Games.xls")
games_sales_dat = pd.read_csv("vgsales-12-4-2019-short.csv")

games_merged_dat = games_dat.merge(games_sales_dat, left_on="Name", right_on="Name", how="left")
print(games_merged_dat)

games_merged_dat.to_csv("output_final_df.csv")

# Defining useful Functions to be used later
def slice_column(input_df, output_df, column, expression=" "):
    unclean = input_df[column].to_list()
    clean = list()
    for record in unclean:
        record = record.split(expression)[0]
        clean.append(record)

    input_df = input_df.drop(columns=[column])
    input_df[column] = clean
    input_df.to_csv(output_df)


def write_joined_df(left, right, output_file, lsuf="new_key"):
    merged = left.join(right, lsuffix=lsuf)
    merged.to_csv(output_file)
