# %%
import pandas as pd

# %%
pd.__version__

# %%
my_series = pd.Series([10,20,30,40,50], index=['a','b','c','d','e'])
my_series

# %%
type(my_series)

# %%
my_series['a']

# %%
my_series['a':'d']

# %%
my_series +5

# %%
my_series

# %%
my_series * 2

# %%
my_series.dtype

# %%
my_series.size

# %%
my_series.shape

# %%
my_series.head()

# %%
my_series.head(2)

# %%
my_series.tail()

# %%
my_series.describe()

# %%
my_series.sort_values(ascending=False)

# %%
data = {"Name": ["John", "Emily","Kate","Sam"],
        "Age":[25,30,28,35],
        "City": ["New york", "San Fransisco", "Chicago", "Seattle"]}
data

# %%
df = pd.DataFrame(data)
df

# %%
data_list =[ ["John", 25, "Newy Work"], ["Emily",30,"San Francisco"],["Kate", 28, "Chicago"], ["Sam", 35, "Seattle"]]

# %%
data_list

# %%
df_list = pd.DataFrame(data_list, columns = ["Name", "Age", "City"])

# %%
df_list

# %%
import numpy as np

# %%
data_array= np.array([[1,2,3],[4,5,6],[7,8,9]])

# %%
data_array

# %%
df_array = pd.DataFrame(data_array, columns = ["A","B","C"])

# %%
type(df_array)

# %%
df_array

# %%
data = {"Name": ["John", "Emily","Kate","Sam"],
        "Age":[25,30,28,35],
        "City": ["New york", "San Fransisco", "Chicago", "Seattle"]}
df = pd.DataFrame(data)
df

# %%
df.to_csv("example.csv", index = False)

# %%
data= pd.read_csv("example.csv")
data

# %%
df

# %%
df.to_excel("example.xlsx", index= False)

# %%
data_excel= pd.read_excel("example.xlsx")
data_excel

# %%
data_excel.rename(columns = {"Age" : "New_Age"})

# %%
data_excel

# %%
df

# %%
df[["Name", "City"]]

# %%
df

# %%
df["Name"]

# %%
df[["Name"]].values

# %%
df

# %%
df[df["Age"] >= 28]

# %%
df[df["Name"]== "John"]

# %%
df

# %%
df[(df["City"]=="New york") & (df["Age"] < 30)]

# %%
selected_cities = ["New york", "Chicago"]

# %%
df[df["City"].isin(selected_cities)]

# %%
data1 = {"A":[1,2,None,4,5],
         "B": [5,7,8,None,10],
         "C": [11,12,13,14,None]}
df = pd.DataFrame(data1)

# %%
df

# %%
df.isnull()

# %%
df.isnull().sum()

# %%
df.dropna()

# %%
df

# %%
df.dropna(inplace = True)

# %%
df

# %%
data1 = {"A":[1,2,None,4,5],
         "B": [5,7,8,None,10],
         "C": [11,12,13,14,None],
         "D": [100,200,300,400,500]}
df = pd.DataFrame(data1)

# %%
df.dropna(thresh=3)

# %%
df.fillna(0)

# %%
df

# %%
df.fillna(df.min())

# %%
df.fillna(method='bfill')

# %%
data = {"A":[1,2,None,4,5],
         "B": [5,7,8,None,10],
         "C": [11,12,13,14,None],
         "D": [100,200,300,400,500]}
df = pd.DataFrame(data, index=['a','b','c','d','e'])
df

# %%
df["A"]

# %%
df[["A"]]

# %%
df.loc["a"]

# %%
df.loc["a":"b"]

# %%
df.loc[["a","e"], ["B","C"]]

# %%
df

# %%
df.iloc[1,3]

# %%
df.iloc[0:3]

# %%
df.iloc[[0,2,4],[0,1]]

# %%
data = {"Name": ["John", "Emily","Kate","Sam"],
        "Age":[25,30,28,35],
        "City": ["New york", "San Fransisco", "Chicago", "Seattle"]}
df = pd.DataFrame(data)
df

# %%
df.iloc[2,2]

# %%
df[df["Age"] < 32]

# %%
df[(df["City"] == "Chicago") & (df["Age"] < 30)] 

# %%
df.query("Age < 32")

# %%
df.query("Age < 30 and City == 'Chicago'")

# %%
df.query("Age *2 > 50 ")

# %%
df.sort_values("Age", ascending= False)

# %%
df.sort_values(["City", "Age"])

# %%
df["Age"].rank()

# %%
data1 = {'A': [1,2,3],
         'B': [4,5,6]}
data2 = {'A':[7,8,9],
         'B':[10,11,12]}
df1= pd.DataFrame(data1)
df2 = pd.DataFrame(data2)

# %%
df1

# %%
df2

# %%
pd.concat([df1,df2])

# %%
pd.concat([df1,df2], axis=1)

# %%
data3 = {'A':[1,2,3],
         'C':[13,14,15]}
df3 = pd.DataFrame(data3)

# %%
pd.merge(df1,df3,on='A')

# %%
df1

# %%
data = { 'A': [1,2,2,3,3],
        'B':[4,5,5,6,7]}
df = pd.DataFrame(data)

# %%
df

# %%
df.drop_duplicates()

# %%
df

# %%
df.drop_duplicates(subset='A')

# %%
df.describe()

# %%
df.isnull()

# %%
df.isnull().sum()

# %%
df.dropna()

# %%
df

# %%
data1 = {"A":[1,2,None,4,5],
         "B": [5,7,8,None,10],
         "C": [11,12,13,14,None]}
df1 = pd.DataFrame(data1)
df1

# %%
df1.dropna()

# %%
df1["A"]

# %%
df1.iloc[2]

# %%
data = {"A":[1,2,None,4,5],
         "B": [5,7,8,None,10],
         "C": [11,12,13,14,None],
         "D": [100,200,300,400,500]}
df2 = pd.DataFrame(data, index=['a','b','c','d','e'])
df2

# %%
df2.loc["a": "c"]

# %%
df2.iloc[[0,2],[0,2]]

# %%
df2.iloc[2]

# %%
df2.iloc[2,2]

# %%
df2.iloc[[2,3]]

# %%
df2.iloc[[2,3],[1,2]]

# %%




