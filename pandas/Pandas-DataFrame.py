import pandas as pd
import numpy as np

#-- Creating Dataframes using list

mylist=['Purushotham','Chandra','Chinna']
df = pd.DataFrame(mylist)
print(df)
print("\n")

#-- Creating Dataframes using Dictionary

mydict={ 'Name': [ 'Purushotham', 'Chinna', 'Ravi' ],
         'Age': [ 28, 22, 23 ] }
df = pd.DataFrame(mydict)
print(df)
print("\n")

#--- Column Selection

mydict={ 'Name': [ 'Purushotham', 'Chinna', 'Ravi' ],
         'Age': [ 28, 22, 23 ],
         'Location': [ 'Chennai', 'Hyderabad', 'Bangalore' ]
         }

df = pd.DataFrame(mydict)

print(df[['Name','Location']])
print("\n")


#-- Row Selection / Indexing a DataFrame using loc 

df = pd.read_csv("C:\\purushotham\\Learning\\python-learning\\Python-practice\\pandas\\nba.csv", index_col="Name")

first=df.loc["Avery Bradley"]
second=df.loc["R.J. Hunter"]
print(first,"\n\n\n",second)
print("\n")

#-- Indexing DataFrame using [] operator

df = pd.read_csv("C:\\purushotham\\Learning\\python-learning\\Python-practice\\pandas\\nba.csv", index_col="Name")
print(df["Age"])
print("\n")
print("\n")

#-- Indexing DataFrame using iloc

df = pd.read_csv("C:\\purushotham\\Learning\\python-learning\\Python-practice\\pandas\\nba.csv", index_col="Name")
print(df.iloc[2])
print("\n")

#-- Working with missing Data

mydict={ 'Name': [ 'Purushotham', 'Chinna', np.nan, 'Ravi' ],
         'Age': [ 28, 22, 23, np.nan ],
         'Location': [ 'Chennai', np.nan, 'Hyderabad', 'Bangalore' ]
         }

df = pd.DataFrame(mydict)

print(df.isnull())
print("\n")
print(df.notnull())
print("\n")
print(df.fillna(0))
print("\n")
print(df.dropna())
print("\n")

#-- Iterating through rows and Columns

mydict={ 'Name': [ 'Purushotham', 'Chinna', 'Ravi' ],
         'Age': [ 28, 22, 23 ],
         'Location': [ 'Chennai', 'Hyderabad', 'Bangalore' ]
         }

df = pd.DataFrame(mydict)

for i,j in df.iterrows():
    print(i, j)
    print()

columns = list(df)
for i in columns:
    print(df[i][2])
