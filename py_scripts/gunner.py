# Cleaning of datasets
# Somewhat main in the beninging

import pandas as pd
import numpy as np

def drop_kick(col_list, dataframe):
    return dataframe.drop(columns=col_list, axis=1)


# Getting the range of years which both datasets share
def year_interval(victim1, victim2, col1, col2):
    return (
        max(victim2[col2].min(), victim1[col1].min()),
        min(victim2[col2].max(), victim1[col1].max()),
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
