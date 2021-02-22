#!/usr/bin/env python
# coding: utf-8

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

# a will be a dataFrame contain all the unique values from column 'Age'
a = df.ix['Age'].unique()

# c will contain all the values satisfied by the condition
c = df.ix['Age']>=30

# select dataFrame will contain all the records whose age is >=30
select = df[df['Age']>=30]
select.to_csv('data1.csv')


# In[10]:


import pandas as pd
import csv

with open("../demo/data.csv","w") as File1:
    write = csv.writer(File1)
    writer = csv.writer(File1)
    writer.writerow(["SN", "Name", "Contribution"])
    writer.writerow([1, "Linus Torvalds", "Linux Kernel"])
    writer.writerow([2, "Tim Berners-Lee", "World Wide Web"])
    writer.writerow([3, "Guido van Rossum", "Python Programming"])

csv_path = "../demo/data.csv"
df = pd.read_csv(csv_path)    
print(df)


# In[23]:


bio_data=[[1, "Linus Torvalds", "Linux Kernel"], 
         [2, "Tim Berners-Lee", "World Wide Web"],
        [3, "Guido van Rossum", "Python Programming"]]


with open("../demo/data1.csv","w") as File1:
    write = csv.writer(File1)
    writer = csv.writer(File1)
    writer.writerow(["SN", "Name", "Contribution"])
    writer.writerows(bio_data)

csv_path = "../demo/data1.csv"
df = pd.read_csv(csv_path)    
print(df)


# In[ ]:




