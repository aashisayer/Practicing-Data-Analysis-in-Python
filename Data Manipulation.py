
# arranging data / ascending as per country
df_sorted_by_country = df.sort_values(by="cost",ascending=True)

print(df_sorted_by_country)

# arranging data as per specific country
print(df[df['country']=='France'])

# arranging data as per specific country and device type

print(df[(df['country']=='France') & (df['device_type']=="PC")])

# mergin two excel sheet data as per order_id

df2 = pd.read_excel("Extra Variable.xlsx")


df['order_id'] = df['order_id'].astype(str)
df2['order_id']=df2['order_id'].astype(str)

merge_df_df2 = df.merge(df2, on='order_id', how='inner')

print(merge_df_df2.shape)

#concatenate extra data

extra_data = "Extra Data.xlsx"
df3 = pd.read_excel(extra_data)
concatenate_df = pd.concat([merge_df_df2,df3], ignore_index=True)
print(concatenate_df.head())
print(concatenate_df.shape)