#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#https://matplotlib.org/
#https://seaborn.pydata.org/
#https://numpy.org/
#https://pandas.pydata.org/


# In[1]:


raw_data = {'Cust_id':[1,2,3,4,5],
           'First Name': ['Alex','John','Haden','James', 'Chris'],
           'Last Name': [ 'Anderson', 'Haris','Mathew','Flintoff','Anderson']}


# In[2]:


raw_data


# In[3]:


import pandas as pd


# In[5]:


customer_details = pd.DataFrame(raw_data)


# In[6]:


customer_details


# In[7]:


raw_data1 = {'c_id': [1,2,3,4,6],
            'Segment': ['Tableau','Python','R','Python','Python'],
            'Sales':[250, 300,275,300,300]}


# In[8]:


sales_details = pd.DataFrame(raw_data1)


# In[9]:


sales_details


# In[10]:


pd.merge(customer_details,sales_details,left_on='Cust_id',right_on='c_id', how='inner')


# In[11]:


pd.merge(customer_details,sales_details,left_on='Cust_id',right_on='c_id', how='left')


# In[12]:


pd.merge(customer_details,sales_details,left_on='Cust_id',right_on='c_id', how='right')


# In[52]:


details = pd.merge(customer_details,sales_details,left_on='Cust_id',right_on='c_id', how='outer')


# In[14]:


pd.concat([customer_details,sales_details], axis=1)


# In[15]:


pd.concat([customer_details,sales_details], axis=0)


# In[32]:


tips = pd.read_csv('C:\\Users\\HP\\Desktop\\Edureka\\Edureka - 29th July - Python Certification Training for Data Science\\Class 4  - DataFrames\\tips.csv')


# In[33]:


del dataset


# In[19]:


import os


# In[20]:


os.getcwd()


# In[21]:


os.chdir('C:\\Users\\HP\\Desktop\\Edureka\\Edureka - 29th July - Python Certification Training for Data Science\\Class 4  - DataFrames\\')


# In[22]:


os.getcwd()


# In[23]:


dataset1 = pd.read_csv('tips.csv')


# In[25]:


del dataset1


# In[34]:


len(tips)


# In[35]:


len(tips.columns)


# In[36]:


tips.columns


# In[37]:


type(tips)


# In[39]:


tips.head()


# In[43]:


tips.tail()


# In[ ]:


select total_bill , tip , smoker , time 
from tips 
limit 5;


# In[45]:


tips[['total_bill','tip','smoker','time']].head()


# In[ ]:


select * from tips 
where time = 'Dinner'
limit 5;


# In[46]:


tips[tips['time']=='Dinner'].head()


# In[ ]:


select * from tips 
where time='Dinner' and tip>5


# In[49]:


tips[(tips['time']=='Dinner') & (tips['tip']>5)]


# In[ ]:


select * from tips where size>=5 or total_bill > 45


# In[51]:


tips[(tips['size']>=5) | (tips['total_bill']>45)]


# In[53]:


details


# In[ ]:


select * from details where cust_is is null


# In[54]:


details[details['Cust_id'].isna()]


# In[ ]:


select * from details where cust_is is not  null


# In[55]:


details[details['Cust_id'].notna()]


# In[ ]:


select sex, count(*)
from tips 
group by sex


# In[56]:


tips.groupby('sex').size()


# In[ ]:


select smoker, sex, count(*)
from tips 
group by smoker , sex


# In[57]:


tips.groupby(['smoker','sex']).size()


# In[59]:


tips['smoker'].count()


# In[60]:


import numpy as np


# In[62]:


df1 = pd.DataFrame(np.array([['a',5,9],['b',4,61],['c',24,9]]),columns=['Name','attr1','attr2'])


# In[63]:


df1


# In[64]:


df2 = pd.DataFrame(np.array([['a',5,19],['b',4,16],['c',2,9]]),columns=['Name','attr3','attr4'])


# In[65]:


df2


# In[66]:


df3 = pd.DataFrame(np.array([['a',5,19],['b',4,16],['e',2,9]]),columns=['Name','attr5','attr6'])


# In[67]:


df3


# In[74]:


pd.merge(pd.merge(df1,df2,on='Name'),df3, on='Name', how='inner')


# In[75]:


df1.merge(df2,on='Name').merge(df3,on='Name')


# In[78]:


df1


# In[79]:


df2


# In[76]:


pd.merge(df1,df2, how='inner', left_on=['Name','attr1'], right_on=['Name','attr3'])


# In[80]:


stats = pd.read_csv('DemographicData.csv')


# In[82]:


len(stats)


# In[83]:


len(stats.columns)


# In[84]:


stats.info()


# In[86]:


stats.describe().transpose()


# In[87]:


stats.columns = ['CountryName','CountryCode','BirthRate','InternetUsers','IncomeGroup']


# In[88]:


stats


# In[89]:


stats = stats.rename(columns={'CountryName':'CN'})


# In[93]:


stats.rename(columns={'CN':'CountryName'}, inplace=True)


# In[94]:


stats


# In[96]:


stats[12:15][['CountryName','IncomeGroup']]


# In[98]:


stats['Mycalc'] = stats.BirthRate * stats.InternetUsers


# In[101]:


stats.sort_values(['Mycalc'],ascending=1)


# In[105]:


stats1 = stats[12:15]


# In[108]:


stats1.insert(5, 'Mycalc', [1,2,3], True)


# In[109]:


stats1


# In[110]:


del stats1


# In[113]:


stats = stats.drop('Mycalc', 1)


# In[114]:


stats


# In[117]:


stats[stats.InternetUsers<2]


# In[118]:


stats.IncomeGroup.unique()


# In[119]:


import matplotlib.pyplot as plt
import seaborn as sns


# In[122]:


sns.lmplot(data=stats, x='InternetUsers',y='BirthRate', fit_reg=False, hue='IncomeGroup')

