#!/usr/bin/env python
# coding: utf-8

# In[24]:


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
pre_process = PolynomialFeatures(degree=3)
pr_model = LinearRegression()
#X_poly
data = pd.read_csv("C:/Users/musto/RepoVC/test/scenario1.csv")
#data


# In[49]:


from collections import defaultdict
out = defaultdict(dict)
types = set(data['type'].values)
predy=[]
pred_=defaultdict(dict)
for type_ in types:
    ides = set(data[data['type'] == type_]['id'])
    for id_ in ides: 
        out[type_ + str(id_)]['x'] = data[(data['type'] == type_)&(data['id'] == id_)]['x']
        out[type_ + str(id_)]['y'] = data[(data['type'] == type_)&(data['id'] == id_)]['y']
    
for obj in out.keys():
    x_axis = pd.DataFrame(out[obj]['x'])
    y_axis = pd.DataFrame(out[obj]['y'])
    X_poly = pre_process.fit_transform(x_axis)
    pr_model.fit(X_poly, y_axis)
    y_pred = pr_model.predict(X_poly)
    predy.append(y_pred)


# In[51]:





# In[48]:


from collections import defaultdict
out = defaultdict(dict)
types = set(data['type'].values)
predy=[]
pred_=defaultdict(dict)
for type_ in types:
    ides = set(data[data['type'] == type_]['id'])
    for id_ in ides: 
        out[type_ + str(id_)]['x'] = data[(data['type'] == type_)&(data['id'] == id_)]['x']
        out[type_ + str(id_)]['y'] = data[(data['type'] == type_)&(data['id'] == id_)]['y']
    
for obj in out.keys():
    x_axis = pd.DataFrame(out[obj]['x'])
    y_axis = pd.DataFrame(out[obj]['y'])
    


# In[44]:


predy.shape


# In[36]:


pda=pd.DataFrame(out['p2']['x'])


# In[33]:


type(out['p2']['x'])


# In[34]:


type(pda)


# In[ ]:




