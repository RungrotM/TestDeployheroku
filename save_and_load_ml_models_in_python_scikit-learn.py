#https://machinelearningmastery.com/save-load-machine-learning-models-python-scikit-learn/ 
#https://blog.datath.com/cheatsheet-pandas/

#%%
#1.save model using pickle
from fileinput import filename
from random import random
from tkinter.font import names
import pandas 
from sklearn import model_selection
from sklearn.linear_model import LogisticRegression
import pickle

#%%
#2.load data
#data="https://raw.githubusercontent.com/jbrownlee/Datasets/master/pima-indians-diabetes.data.csv"
data=r"data_test_save_load_ml.csv"
names=['preg','plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age','class']
dataframe=pandas.read_csv(data, names=names)
dataframe
# %%
#3.feature enginer
array=dataframe.values #convert dataframe to array
array
# %%
# prepare data for train
X=array[:,0:8] # drop colomn class [data for training model]
Y=array[:,8] #column class [data for validation]
test_size=0.33
seed=7
# %%
#train test split
X_train, X_test, Y_train, Y_test = model_selection.train_test_split(X,Y,test_size=test_size,random_state=seed)

# %%
#4.training  model 
model=LogisticRegression() #create model 
model.fit(X_train,Y_train) 
# %%
#5.save the model to disk
filename='test_save_and_load_model.sav'
pickle.dump(model,open(filename, 'wb'))

# %%
#6.load model
load_model=pickle.load(open(filename,'rb'))
result=load_model.score(X_test, Y_test)
print(result)
# %%
