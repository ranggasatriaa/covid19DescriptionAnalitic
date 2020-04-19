#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
import stemgraphic
get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


# init csv
# data: https://www.kaggle.com/kimjihoo/coronavirusdataset
csv = pd.read_csv('data2/PatientInfo.csv')
PI = csv[['patient_id','birth_year','province','city','infection_case','confirm_date']].dropna()
PI


# In[3]:


dataByBirth = PI.groupby('birth_year')['patient_id'].count()
dataByProvince = PI.groupby('province')['patient_id'].count()
dataByCity = PI.groupby('city')['patient_id'].count()
dataByCase = PI.groupby('infection_case')['patient_id'].count()
dataByConfirm = PI.groupby('confirm_date')['patient_id'].count()


# ### Select the data to be executed

# In[4]:


# Select Data
selectedData = dataByBirth


# # Organize Data

# In[5]:


freq_table = selectedData.reset_index()
freq_table.rename(columns={'patient_id':'frequency'},inplace=True)
freq_table.sort_values(by=['frequency'])


# ## Frequency Distribution

# In[6]:


freq_table.insert(2, "Relative Frequency", freq_table.frequency/freq_table.frequency.sum()*100, True) 
freq_table.insert(3, "Cumulative Relative Frequency", (freq_table.frequency/freq_table.frequency.sum()*100).cumsum(), True) 
freq_table


# ## Histogram

# In[7]:


selectedData.hist()


# ## Steam Leaf

# In[8]:


fig, ax = stemgraphic.stem_graphic(selectedData)


# ## Central Tendency

# In[9]:


print ("Total nilai : ",selectedData.sum())
print ("Jumlah data : ",selectedData.count())
print ("Mean   : ",selectedData.mean())
print ("Median : ",selectedData.median())
print ("Mode   : ")
print (selectedData.mode())


# ## Variance 

# In[10]:


print('Range   ',selectedData.max()-selectedData.min())
print('Variance',selectedData.var())
print(selectedData.describe())


# In[11]:


data = selectedData
data.plot(kind='line',figsize=(20,10))


# In[12]:


data = selectedData
data.plot(kind='bar',figsize=(20,10))

