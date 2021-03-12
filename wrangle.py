import warnings
warnings.filterwarnings("ignore")

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import env

from sklearn.model_selection import train_test_split


def get_connection(db, user=env.user, host=env.host, password=env.password):
    return f'mysql+pymysql://{user}:{password}@{host}/{db}'
    
    
## contract type 3 == two year contract

sql = '''
select customer_id, monthly_charges, tenure, total_charges
from customers
where contract_type_id = 3;
'''


def wrangle_telco():
    data = pd.read_csv("wrangle_telco.csv")
    
    data = data.set_index("customer_id")
    
    data['total_charges'].replace(r'^\s*$', np.nan, regex=True, inplace=True)
    # replace white space objects with NaN
    
    data = data.dropna()
    # remove all NaN values
    
    data.total_charges = data.total_charges.astype('float')
    # converts total_charges from object to float
        
    return data


def split(df, stratify_by=None):
    """
    Crude train, validate, test split
    To stratify, send in a column name
    """
    
    if stratify_by == None:
        train, test = train_test_split(df, test_size=.2, random_state=319)
        train, validate = train_test_split(train, test_size=.3, random_state=319)
    else:
        train, test = train_test_split(df, test_size=.2, random_state=319, stratify=df[stratify_by])
        train, validate = train_test_split(train, test_size=.3, random_state=319, stratify=train[stratify_by])
    
    return train, validate, test


