""" Lambdata - a colledtion of Data Science helper functions"""
import pandas as pd 
import numpy as np 

def df_cleaner(df):
    """Clean a DF of null values"""
    df = df.dropna()
    return df

def randomize(df):
    """Randomize a dataframe"""
    df=df.iloc[np.random.permutation(df.index)].reset_index(drop=True)
    return df
