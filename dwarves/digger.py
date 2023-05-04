# Getting and combining data
import pandas as pd
import numpy as np
import scout
from numpy import ndarray
from scipy.stats import binned_statistic


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


def slam_dunk(dataset, column, labels):
    min_value = dataset[column].min()
    max_value = dataset[column].max()
    print("min: ", min_value, " max: ", max_value)
    bins = np.linspace(min_value, max_value, len(labels) + 1)

    dunked_column = "bin_" + column
    dataset[dunked_column] = pd.cut(
        dataset[column], bins=bins, labels=labels, include_lowest=True
    )

    dataset = scout.cure_depression(dataset)

    x_data = np.arange(0, len(dataset))
    y_data = dataset[column]
    x_bins, bin_edges, misc = binned_statistic(
        y_data, x_data, statistic="median", bins=len(labels)
    )
    bin_intervals = pd.IntervalIndex.from_arrays(bin_edges[:-1], bin_edges[1:])
    dataset["bin_value"] = dataset[column].apply(
        lambda x: set_to_median(x, bin_intervals)
    )

    return dataset


def set_to_median(x, bin_intervals):
    for interval in bin_intervals:
        if x in interval:
            return interval.mid
