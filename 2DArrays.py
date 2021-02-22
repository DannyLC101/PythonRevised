#!/usr/bin/env python
# coding: utf-8

# In[12]:


# 2D Arrays
import numpy as np
a = [[11,12,12], [21,22,23], [31,32,33]]
A = np.array(a)
print(A)
print(np.ndim(A)) # ndim will return dimension of array
print(np.shape(A)) # return #of rows and #of columns
print(np.size(A)) # #of elements in array
print(A[0][0])
print(A[0:2,2]) # [0,1][2]


# In[14]:


# Addition of array
# Same way we can do -,*,+2

import numpy as np
X = np.array([[1,0],[0,1]])
Y = np.array([[2,1],[1,2]])
Z = X + Y
print(Z)


# In[16]:


# LINEAR Multiplication
import numpy as np
X = np.array([[0,1,0],[0,1,2]])
Y = np.array([[1,2],[3,4],[5,6]])
Z = np.dot(X,Y)
# ([0,1,0]*[1][3][5]) + ([0,1,2]*[2][4][6])
print(Z)


# In[ ]:





# In[ ]:




