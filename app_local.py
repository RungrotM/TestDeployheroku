#%%
#1.import library 
import pickle
import numpy as np 
from flask import Flask, request

#%%
#2.setting parameter 
app=Flask(__name__)
model=pickle.load(open('model.pk','rb'))
# %%
#3.create root url and fucntion for prediction 
@app.route('/prediction',methods=['POST','GET'])
def prediction():
    if request.method=='GET':
        return 'Resend with post method'

    elif request.method=='POST' :
        X=request.get_json()

        x1=X['x1']
        x2=X['x2']
        x3=X['x3']
        XTest=np.array([[x1,x2,x3]])

        predicted=model.predict(XTest)[0]
        predicted=1/(1+np.exp(-predicted))
        return str(predicted.round(4))

# %%
if __name__== '__main__':
    app.run(debug=True)
# %%
