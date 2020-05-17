import os
import numpy as np
import pandas as pd
from pandas.api.types import CategoricalDtype #For definition of custom categorical data types (ordinal if necesary)
import matplotlib.pyplot as plt
import seaborn as sns  # For hi level, Pandas oriented, graphics
import scipy.stats as stats  # For statistical inference 
import pandas_profiling
from pandas_profiling import ProfileReport
import pickle



os.chdir('/Users/salim/Desktop/MERCADONA_TECH/')
del(product_categories_df)

#load the data
product_categories_df = pd.read_csv ("product_categories_df.csv", sep=',', decimal='.')


fraud_df = pd.read_csv("fraud_df.csv",sep =',', decimal='.')
fraud_df['Target']='Yes'


non_fraud_df = pd.read_csv("non_fraud_df.csv",sep =',', decimal='.')
non_fraud_df['Target']='No'


#merged_fraud_df = non_fraud_df.merge(fraud_df, left_on='Target',right_on='Target')
concatenated_fraud_df = pd.concat([non_fraud_df, fraud_df])
concatenated_fraud_df.columns



country_codes_df = pd.read_csv("wikipedia-iso-country-codes.csv",sep=',', decimal='.')



#Explore the data 
report_product_categories_df = ProfileReport(product_categories_df, title='Pandas Profiling Report', html={'style':{'full_width':True}})
report_product_categories_df.to_file("report_product_categories_df.html")

fraud_df = ProfileReport(fraud_df, title='Pandas Profiling Report', html={'style':{'full_width':True}})
fraud_df.to_file("fraud_df.html")




non_fraud_df = ProfileReport(non_fraud_df, title='Pandas Profiling Report', html={'style':{'full_width':True}})
non_fraud_df.to_file("non_fraud_df.html")


country_codes_df = ProfileReport(country_codes_df, title='Pandas Profiling Report', html={'style':{'full_width':True}})
country_codes_df.to_file("country_codes_df.html")


with open('product_categories.pkl','rb') as file:
    data=pickle.load(file)

