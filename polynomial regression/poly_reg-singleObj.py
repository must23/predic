#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


# In[3]:


pedestrian_data = pd.read_csv("C:/Users/musto/RepoVC/97_33.csv")


# In[4]:


X = pedestrian_data[["x"]]
y = pedestrian_data[["y"]]


# In[5]:


from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
pre_process = PolynomialFeatures(degree=3)
X_poly = pre_process.fit_transform(X)
#X_poly


# In[20]:


pr_model = LinearRegression()
# Fit our preprocessed data to the polynomial regression model
pr_model.fit(X_poly, y)
# Store our predicted Y values in the variable y_pred
y_pred = pr_model.predict(X_poly)


# In[21]:


# Plot our model on our data
plt.scatter(X, y, c = "black")
plt.xlabel("X_axis")
plt.ylabel("Y_axis")
plt.plot(X, y_pred, c = "red")


# In[16]:


next_y= pr_model.predict(pre_process.fit_transform([[4]]))


# In[8]:


"""theta0 = pr_model.intercept_
_, theta1, theta2 = pr_model.coef_
theta0, theta1, theta2"""

"""
m=pr_model.coef_[0]
b=pr_model.intercept_
print("slope=",m, "intercept=",b)"""

theta1 = pr_model.coef_
theta1


# In[22]:


#last x position
last_x= pedestrian_data['x'].iloc[-1]


# In[23]:


last_x


# In[31]:


mean=abs(X.mean(axis=0))  


# In[32]:


mean


# In[33]:


post_predicted_list=[]


# In[35]:


for i in np.arange (last_x, last_x+8, mean[0]/5):
    next_y= pr_model.predict(pre_process.fit_transform([[i]]))
    post_predicted_list.append([i, next_y[0][0]])


# In[36]:


post_predicted_list


# In[19]:


#evaluating error, the lower the better
from sklearn.metrics import mean_squared_error
mean_squared_error(y, y_pred)


# In[ ]:




