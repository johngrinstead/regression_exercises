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
    
    correlation = train.corr()
    # makes a readable correlation report
    
    return pairplot, correlation


def months_to_years(df):
    df['tenure_years'] = (df['tenure'] / 12).round(0).astype('int')
    
    return df


