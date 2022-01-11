#%%
import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv('FoodPrice_in_Turkey.csv')
df

# %%
# Xóa các dòng có thuộc tính ProductID trùng nhau, 
# giữ lại bản ghi cuối cùng, giữ chỉ số ban đầu của các dòng
df=df.drop_duplicates(['ProductId'], keep='last')
df

# %%
df=df.drop_duplicates(['ProductId'], keep='last').reset_index(drop=True)
df

# %%
# Tách file chứa thông tin sản phẩm
df_pro = df.loc[:,['ProductId','ProductName','UmId','UmName']]
df_pro

# %%
# Tách file chứa thông tin giá với số dòng từ bản ghi 10 đến 20
df_pri10 = df.loc[10:20,['ProductId','Place','Month','Year','Price']]
df_pri10

# %%
df_pri = df.loc[:,['ProductId','Place','Month','Year','Price']]
df_pri

# %%
df1=pd.merge(df_pro,df_pri, on='ProductId')
df1

# %%
df2=pd.concat([df_pro,df_pri], axis=1)
df2

# %%
