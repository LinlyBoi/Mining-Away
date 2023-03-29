# Regression/Prediction (Totally gonna do later trust bro)

from sklearn.impute import SimpleImputer
import numpy as np


# Column2 is the column you're grouping by using the given values pls
def cure_depression(dataset, column, column2, values):
    # Allegedly for loop here )
    dataset[column].fillna(dataset[column].mean(), inplace=True)
    #    print(dataset)
    return dataset[column].to_list()
