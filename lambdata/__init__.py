""" Lambdata - a colledtion of Data Science helper functions"""
import pandas as pd 
import numpy as np 

def df_cleaner(df):
    """Clean a DF of null values"""
    df = df.dropna()
    return df

def randomize(df):
    """Randomize the rows of a dataframe"""
    df=df.iloc[np.random.permutation(df.index)].reset_index(drop=True)
    return df

class Unknown:
    def __init__(self, df):
        self.df = df

    def drop_nulls(self):
        self.df = df.dropna()
        return self.df

    def random_df(self):
        self.df = df.iloc[np.random.permutation(df.index)].reset_index(drop=True)
        return self.df


