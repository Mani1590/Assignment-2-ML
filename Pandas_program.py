#!/usr/bin/env python
# coding: utf-8

# In[7]:


# Write a Pandas program to convert Series of lists to one Series.
import pandas as pd
series_list=pd.Series([[1,2,3],[4,5,6,7],[8,9,10]])
print(series_list)
one_series=series_list.explode()
print(one_series)


# In[10]:


# Write a Pandas program to create a subset of a given series based on value and condition.
import pandas as pd
data={'A':10, 'B': 100, 'C': 30, 'D': 40, 'E': 50}
series_list=pd.Series(data)
print(series_list)
subset_series=series_list[series_list>30]
print(subset_series)


# In[25]:


# Write a Pandas program to display most frequent value in a given series and replace everything else as 'Other' in the series.
import pandas as pd
data = pd.Series(['mani', 'varshi', 'mani', 'santhosh', 'varshi', 'sai', 'santhosh', 'heman'])
most_frequent_value = data.value_counts().idxmax()
data.replace(to_replace=data[data != most_frequent_value].unique(), value='other', inplace=True)
print(data)


# In[12]:


# Write a Pandas program to find the positions of numbers that are multiples of 5 of a given series.
import pandas as pd
data=pd.Series([1,2,3,4,5,6,7,8,9,10])
print(data)
result=data[data%5==0].index
print(result)


# In[13]:


# Write a Pandas program to calculate the number of characters in each word in a given series. 
import pandas as pd
data = pd.Series(['Mani', 'Kiran', 'Sai', 'Teja'])
print(data)
word_lengths = data.str.split().apply(lambda x: [len(word) for word in x])
print(word_lengths)


# In[14]:


# Write a Pandas program to convert year-month string to dates adding a specified day of the month.
import pandas as pd
year_month_series = pd.Series(['2024-01', '2024-02', '2024-03'])
day_of_month = 15
result_dates = pd.to_datetime(year_month_series + '-' + str(day_of_month), format='%Y-%m-%d')
print(year_month_series)
print(result_dates)


# In[15]:


# Write a Pandas program to create and display a DataFrame from a specified dictionary data which has the index labels.
import pandas as pd
data_dict = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [25, 30, 35, 40],
    'City': ['New York', 'San Francisco', 'Los Angeles', 'Chicago']
}
index_labels = ['Person1', 'Person2', 'Person3', 'Person4']
df = pd.DataFrame(data_dict, index=index_labels)
print(df)


# In[16]:


# Write a Pandas program to select the rows where the number of attempts in the examination is greater than 2.
import pandas as pd
data = {
    'Student': ['Alice', 'Bob', 'Charlie', 'David'],
    'Attempts': [1, 3, 2, 4],
    'Score': [80, 65, 90, 75]
}
exam_data = pd.DataFrame(data)
selected_rows = exam_data[exam_data['Attempts'] > 2]
print(exam_data)
print(selected_rows)


# In[18]:


# Write a Pandas program to append a new row &#39;k&#39; to data frame with given values for each column. Now delete the new row and return the original DataFrame.
import pandas as pd
data = {
    'Student': ['Alice', 'Bob', 'Charlie', 'David'],
    'Attempts': [1, 3, 2, 4],
    'Score': [80, 65, 90, 75]
}
exam_data=pd.DataFrame(data)
print(exam_data)
new_row={'Student': 'Eve', 'Attempts': 2, 'Score': 85}
exam_data=exam_data.append(new_row,ignore_index=True)
print(exam_data)
exam_data=exam_data.drop(exam_data[exam_data['Student']=='Eve'].index)
print(exam_data)


# In[19]:


# Write a Pandas program to sort the DataFrame first by 'name' in descending order,then by 'score' in ascending order.
import pandas as pd
data = {
    'Student': ['Alice', 'Bob', 'Charlie', 'David'],
    'Attempts': [1, 3, 2, 4],
    'Score': [80, 65, 90, 75]
}
series_list=pd.DataFrame(data)
print(series_list)
sorted_list=series_list.sort_values(by=['Student','Score'],ascending=[False,True])
print(sorted_list)


# In[21]:


# Write a Pandas program to replace the 'qualify' column contains the values &#39;yes&#39; and 'no' with True and False.
import pandas as pd
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Qualify': ['yes', 'no', 'yes', 'no'],
    'Score': [80, 65, 90, 75]
}
exam_data=pd.DataFrame(data)
print(exam_data)
exam_data['Qualify']=exam_data['Qualify'].replace({'yes':True,'no':False})
print(exam_data)


# In[22]:


# Write a Pandas program to remove infinite values from a given DataFrame.
import pandas as pd
import numpy as np
data = {
    'A': [1, 2, np.inf, 4],
    'B': [5, 6, 7, 8]
}
df = pd.DataFrame(data)
print(df)
df.replace([np.inf, -np.inf], np.nan, inplace=True)
df.dropna(inplace=True)
print(df)


# In[ ]:




