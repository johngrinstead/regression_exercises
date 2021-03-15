import matplotlib.pyplot as plt
import seaborn as sns

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
import warnings
warnings.filterwarnings("ignore")


def plot_variable_pairs(df):
    pairplot = sns.pairplot(df, kind = 'reg', height=3)
    # creates a pairplot that includes a regression line
    
    correlation = df.corr()
    # makes a readable correlation report
    
    return pairplot, correlation


def months_to_years(df):
    df['tenure_years'] = (df['tenure'] / 12).round(0).astype('int')
    
    return df


def plot_categorical_and_continuous_vars(df, cat_vars, quant_vars, target_var):
    plot_cat(df, cat_vars)
    
    plot_quant(df, quant_vars)
    
    
def plot_cat(df, cat_vars):
    for col in list(df.columns):
        if col in cat_vars:
            sns.distplot(df[col])
            plt.show()
            
            
def plot_quant(df, quant_vars):
    for col in list(df.columns):
        if col in quant_vars:
            sns.boxplot(data = df, y = col)
            plt.show()
            
            
