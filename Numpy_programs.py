#!/usr/bin/env python
# coding: utf-8

# In[4]:


# Write a NumPy program to multiply two given arrays of same size element-by-element.
import numpy as np
array1=np.array([1,4,5,6])
array2=np.array([3,4,7,12])
result=np.multiply(array1,array2)
print(result)


# In[6]:


# Write a NumPy program to find the missing data in a given array.
import numpy as np
data=np.array([2.5,4.5,np.nan,6.4,np.nan])
missing=np.isnan(data.astype(float))
print(missing)
indices=data[missing]
print(indices)


# In[8]:


# Write a NumPy program to test whether each element of a 1-D array is also present in a second array.import numpy as np
array1=np.array([1,4,5,6])
array2=np.array([3,4,7,5])
result=np.isin(array1,array2)
print(result)


# In[9]:


# Write a NumPy program to save a NumPy array to a text file.
import numpy as np
my_array = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
file_path = "text_file.txt"
np.savetxt(file_path, my_array, fmt='%d', delimiter=', ')
print(f"Array has been saved to {file_path}.")


# In[10]:


# Write a NumPy program to Create a 1-D array of 30 evenly spaced elements between 2.5. and 6.5, inclusive.
import numpy as np
result=np.linspace(2.5,6.5,30)
print(result)


# In[ ]:




