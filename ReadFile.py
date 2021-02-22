#!/usr/bin/env python
# coding: utf-8

# In[9]:


File1 = open("../demo/text1.txt", "r") 
#mode can be r for read, w for write, a for append
#don't forget to close the file at the end

# with will automatically close the file
# read() will read a complete file and store it in a variable
with open("text1.txt", "r") as File1:
    file_stuff = File1.read()
    print(file_stuff)
print(File1.closed)
print(file_stuff)


# In[10]:


File1 = open("../demo/text1.txt", "r") 

# readlines() will store each line as a String value in variable
# file_stuff is a List
with open("text1.txt", "r") as File1:
    file_stuff = File1.readlines()
    print(file_stuff)
print(File1.closed)
print(file_stuff)


# In[15]:


File1 = open("../demo/text1.txt", "r") 

# readline() will single line at a time and store it in a variable
with open("text1.txt", "r") as File1:
    file_stuff = File1.readline() # reads 1st line
    print(file_stuff)
    file_stuff = File1.readline() # reads 2nd line
    print(file_stuff)
    file_stuff = File1.readline() # reads 3rd line
    print(file_stuff)
print(File1.closed)
print(file_stuff)


# In[16]:


File1 = open("../demo/text1.txt", "r") 

# for loop to read each line from a file
with open("text1.txt", "r") as File1:
    for l in File1:
        print(l)
print(File1.closed)


# In[34]:


# File1 = open("../demo/text1.txt", "r") 

# readline(n) n characters of a line will be printed
with open("text1.txt", "r") as File1:
    file_stuff=File1.readline(1)
    print(file_stuff)
    file_stuff=File1.readline(5)
    print(file_stuff)
    file_stuff=File1.readline(9)
    print(file_stuff)
    file_stuff=File1.readline(5)
    print(file_stuff)
    file_stuff=File1.readline(9)
    print(file_stuff)
print(File1.closed)


# In[40]:


# write data into file
File1 = open("../demo/text2.txt", "w") 

# it will create a text2.txt file in the directory
with open("text2.txt", "w") as File1:
    File1.write("This is line 4")
with open("text2.txt", "r") as File1:
    file_stuff = File1.read()
    print(file_stuff)
print(File1.closed)


# In[45]:


line_list = ["This is line A\n", "This is line B\n", "This is line C\n"]
with open("../demo/text2.txt", "w") as File1:
    for l in line_list:
        File1.write(l)
with open("text2.txt", "r") as File1:
    file_stuff = File1.read()
    print(file_stuff)
print(File1.closed)


# In[46]:


# this will read lines from text2 and write to text1
with open("../demo/text2.txt", "r") as FileRead:
    with open("../demo/text1.txt", "w") as FileWrite:
        for l in FileRead:
            FileWrite.write(l)
print(FileRead.closed)
print(FileWrite.closed)


# In[ ]:




