import warnings
warnings.filterwarnings("ignore")

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import env


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
    
    data['total_charges'].replace(r'^\s*$', np.nan, regex=True, inplace=True)
    # replace white space objects with NaN
    
    data = data.dropna()
    # remove all NaN values
    
    data.total_charges = data.total_charges.astype('float')
    # converts total_charges from object to float
    
    df = data.drop(columns='Unnamed: 0', inplace=True)
    
    df = data.drop(columns='customer_id', inplace=True)
    
    
    
    return data


