Description:
- Load Excel data into a Pandas DataFrame
- Handle missing values
- Correct inconsistent values
- Fix misidentified data types
- Prepare data for analysis

import os
print (os.getcwd())
os.chdir("C:/Users/Aashis/Documents/Data Analysis Sample File")
print (os.getcwd())

import pandas as pd
sample_sales_data = "sample sales data.xlsx"
df=pd.read_excel(sample_sales_data)
print(df.head())

missing_values = df.isnull().sum()
print(missing_values[missing_values>0])

from sklearn.impute import SimpleImputer
missing_column1 = "order_value_EUR"
missing_column2 = "device_type"
imputer1 = SimpleImputer(strategy='median')
imputer2= SimpleImputer(strategy='most_frequent')
df[[missing_column1]]=imputer1.fit_transform(df[[missing_column1]])
df[[missing_column2]]=imputer2.fit_transform(df[[missing_column2]])

missing_values = df.isnull().sum()
print(missing_values[missing_values>0])

print(df.dtypes)

cost = df['cost']
date = df['date']
order_id=df['order_id']
non_numeric_cost= []
non_date=[]
non_numeric_order_id=[]

for value in cost:
    if isinstance(value,str) and not value.isnumeric():
        non_numeric_cost.append(value)

print(non_numeric_cost)

non_numeric_data_type = ['cost','order_id']
df[non_numeric_data_type]= df[non_numeric_data_type].apply(pd.to_numeric, errors='coerce')
df['date'] = pd.to_datetime(df['date'],errors='coerce')
print(df.dtypes)

