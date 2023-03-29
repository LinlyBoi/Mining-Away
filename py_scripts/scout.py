# Regression/Prediction (Totally gonna do later trust bro)

from sklearn.impute import SimpleImputer
import numpy as np


def cure_depression(dataset, column):
    dataset[column].fillna(dataset[column].mean(), inplace=True)
    print("what you want")
    print(dataset)
    return dataset[column].to_list()
