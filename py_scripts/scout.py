# Regression/Prediction (Totally gonna do later trust bro)
from sklearn.linear_model import LinearRegression
from sklearn.impute import SimpleImputer
from sklearn import preprocessing
import numpy as np
import pandas as pd


def cure_depression(dataset):
    # this is pog
    numeric = dataset.select_dtypes(include=np.number)
    numeric_columns = numeric.columns
    dataset[numeric_columns] = dataset[numeric_columns].interpolate(
        method="linear", limit_direct="forward"
    )
    # fuck around and find out with other methods maybe idk
    return dataset


# Fuck you and whateevr you fucking stand for you dumb whore faggot
def regression_expression(dataset, column, missing_value):
    lr = LinearRegression()
    numeric = dataset.select_dtypes(include=np.number)
    # Migrate this to digger
    # the fookin nulls
    testdf = numeric[numeric[column].isnull() == False]
    testdf = testdf[testdf[column] != 0]
    # the non nulls and non 0s
    traindf = numeric[numeric[column].isnull() == False]
    traindf = traindf[traindf[column] != 0]
    # print(traindf.head(20))
    # end of migration

    y = traindf[column]
    traindf.drop(column, axis=1, inplace=True)
    lr.fit(traindf, y)
    pred = lr.predict(testdf)
    # can't put this in data set directly because length no match
    # join testdf and traindf to form dataset perhaps??
    testdf[column] = pred
    print(testdf.head(30))

# https://scikit-learn.org/stable/modules/preprocessing.html#preprocessing
# That helps ^
# This boi should work, idk i'm implementing blindly
def scaling_zscore(datashitter, col):
    scaler = preprocessing.StandardScaler().fit(datashitter[col])
    return scaler.transform(datashitter[col])

def scaling_range(datashitter, col):
    nonnull = datashitter[col].isna()
    minmax_scaler = preprocessing.MinMaxScaler()
    trainer = minmax_scaler.fit_transform(datashitter[nonnull])
    return minmax_scaler.transform(datashitter[col])
