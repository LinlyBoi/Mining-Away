# Getting and combining data
import pandas as pd
import numpy as np

# reading the data
# -> MAKE SURE OF THE DATA FRAMES NAMES PEFORE YOU RUN IT


df1 = pd.read_csv("output_6th_df.csv")
df2 = pd.read_csv("vgsales-12-4-2019-short.csv")


# ----------------------------------------------------------


# print(pf1.head)
# print(pf2.head)

# ---------------------------------------------------------


#                    merging

combined_df = df1.merge(df2, left_on="Name", right_on="Name", how="left")
print(combined_df)
combined_df.to_csv("output_final_df.csv")
df = combined_df

# ---------------------------------------------------------


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
