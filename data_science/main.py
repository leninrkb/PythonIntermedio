import pandas as pd

# data frame df
df_train = pd.read_csv('train.csv')

# first n elements
df_train.head(20)

# returs columns x rows (x,y)
df_train.shape

# view specific column
df_train['column_name']

# multiple columns
df_train[['name','name2','name_n']]

# mean
df_train['column_name'].mean()

# summary of df
df_train.describe()

import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from scipy.stats import norm
from sklearn.preprocessing import StandardScaler
from scipy import stats
import warnings

# to watch plots inline 
# %matplotlib inline

df_train['SalePrice'].describe()

# plot 
sns.distplot(df_train['SalePrice'])

# skew & kurt
df_train['SalePrice'].skew()







