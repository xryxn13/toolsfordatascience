#!/usr/bin/env python
# coding: utf-8

# # this is an introductory sentence

# In[2]:


List1=['R,SQL,Java,Julia,Scala,JavaScript,Swift']
List1


# In[3]:


List2 = ['Numpy,Keras,Pandas,Scipy,TensorFlow']
List2


# In[4]:


List3=['SAS,BigML,MATLAB,Excel,ggplot2,Jupyter,Skit-learn,TensorFlow']
List3


# In[5]:


List4 = 1+2+4+5
List4


# In[6]:


List5=1+3*8
List5


# In[17]:


List6=['apple,Banana,Orange,Cherry,Jack,Lisa']

List6


# In[18]:


List7=['William Shakespeare,gatha Christie ,Harold Robbins']
List7


# In[ ]:


days = 0
hours = 0
mins = 0

time = 200
#days = time / 1440
leftover_minutes = time % 1440
hours = leftover_minutes / 60
#mins = time - (days*1440) - (hours*60)
print(str(days) + " days, " + str(hours) + " hours, " + str(mins) +  " mins. ")

# Result: 3.3333333333333335 hours

