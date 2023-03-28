# Getting and combining data
import pandas as pd
import numpy as np


# Defining useful Functions to be used later
def slice_column(input_df, column, expression=" "):
    unclean = input_df[column].to_list()
    clean = list()
    for record in unclean:
        record = record.split(expression)[0]
        clean.append(record)

    input_df = input_df.drop(columns=[column])
    input_df[column] = clean
    return input_df


def write_joined_df(left, right, lsuf="new_key"):
    merged = pd.concat([left, right], sort=False, ignore_index=True)  # Good
    return merged
