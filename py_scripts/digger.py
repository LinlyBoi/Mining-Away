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

df_compine = df1.merge(df2, left_on="Name", right_on="Name", how="left")
print(df_compine)
df_compine.to_csv("output_final_df.csv")
df = df_compine
output_df = "N There U Have It"

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
