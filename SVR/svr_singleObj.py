import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.svm import SVR
from sklearn.metrics import r2_score,mean_squared_error
import matplotlib.pyplot as plt

df = pd.read_csv("C:/Users/musto/RepoVC/93_1.csv")
x=df.x.values.reshape(-1,1)
y=df.y.values.reshape(-1,1)

x_train, x_test, y_train, y_test = train_test_split(x,y, test_size=0.40, random_state=42)

SupportVectorRegModel=SVR()
SupportVectorRegModel.fit(x_train, np.ravel(y_train,order='C'))

y_pred=SupportVectorRegModel.predict(x_test)
y_pred

mse=mean_squared_error(y_test, y_pred)
mse
