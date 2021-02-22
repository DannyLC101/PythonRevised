#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas
# Pandas built-in functions
# read_csv()
# Series()
# DataFrame
# values

csv_path = "big.csv"
df = pandas.read_csv(csv_path) 


# In[ ]:


# writing 'pandas' everytime is tidious method
# instead we can write the abbreviation in import line
import pandas as pd
csv_path = "big.csv"
df = pd.read_csv(csv_path)
# result from the file is stored in variable df

df.head() #will read 1st 5 rows of dataframe


# In[3]:


#read excel file
xlsx_path="file1.xlsx"
df=pd.read_excel(xlsx_path)
df.head()


# In[ ]:


bio_data={'Name':["Tom", "Sam", "Elsa", "Siri", "Cortana"], 
         'Age':[22,23,34,43,23],
         'City':["Chicago","NYC","Huston","Denver","Miami"]}
# keys corresponds to table headers
# values are list corresponding to rows


# In[ ]:


# bio_data={'Name':["Tom", "Sam", "Elsa", "Siri", "Cortana"], 
#          'Age':[22,23,34,43,23],
#          'City':["Chicago","NYC","Huston","Denver","Miami"]}

import pandas as pd
csv_path = "big.csv"
df = pd.read_csv(csv_path)
x=df[['Name']] # x will contain all the values of column 'Name'
y=df[['Name','Age','City']] #y will contain all the values of column Name, Age and City
#x and y is the resultant dataFrame derived from original dataFrame(table)

#Access 1st row and 1st column
name1=df.ix[0,0] # value of name1 will be "Tom"

#df.ix[0,1]:22
#df.ix[1,1]:23
#df.ix[2,2]:"Huston"
#df.ix[2,"Name"]:"Elsa"
#df.ix[0:1, 0:2]: will display 1st 2 rows and 1st 3 columns
#df.ix[0:1, 'Name':'City']: will display 1st 2 rows and all the columns between Name and City


# In[ ]:





# In[ ]:




