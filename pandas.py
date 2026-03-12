  
  --------------PANDAS------------
# DataSeries:
#a. Write a Pandas program to create and display a one-dimensional 
#array-like object containing an array of data using Pandas module.
#b. Write a Pandas program to convert a Panda module Series to Python
#  list and it's type.
 
import pandas as pd
import numpy as np

data_list = pd.Series([1,2,3,77,-55])

print(data_list)

data__list = data_list.tolist() 
print(data__list)


names=pd.Series(["shanmukh","loves","kavya","but","kavya","didn't","shanmukh"])
print(names)

names_list=names.tolist()
print(names_list)
-------------------------------------------------
  
  #Pandas DataFrames:
#Consider Sample Python dictionary data and list labels:
#exam_data = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael',
#'Matthew', 'Laura', 'Kevin', 'Jonas'],
#'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
#'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
#'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}
#labels = ['a', 'b', 'c', 'd', 'e', 'f, 'g', 'h', 'i', 'j']


#a. Write a Pandas program to create and display a DataFrame from a specified
#dictionary data which has the index labels.
import pandas as pd
import numpy as np


exam_data = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael','Matthew', 'Laura', 'Kevin', 'Jonas'],
    'score': [12.5, 9, 16.5, np.nan, 9, 20,14.5, np.nan, 8, 19],
    'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
    'qualify':  ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

#syntax df = pd.DataFrame(data,index=index_label)
df = pd.DataFrame(exam_data,index = labels)
print("DataFrame created from the dictionary:")
print(df)

#b. Write a Pandas program to change the name 'James' to 'Suresh' in name column of
#the DataFrame.

#syntax df.loc['row_value','column_value']=value
df.loc['d','name'] = 'Suresh'
print(df)


#c. Write a Pandas program to insert a new column in existing DataFrame.

salaries = [50000,60000,75000,450000,55000,70000,48000,62000,78000,65000]
#syntax df['new_column'] = values
df['salary'] = salaries
print(df)

#iv)Write a Pandas program to get list from DataFrame column headers

#syntax my_list = df['column_name'].tolist()
column_headers = df.columns.tolist()
print(column_headers)

----------------------------------------------
