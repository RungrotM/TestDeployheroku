#%%
import requests

URL='http://127.0.0.1:5000/prediction'


X={
    'x1':0.019287,
    'x2':-0.05005,
    'x3':0.08493
}
r=requests.post(URL, json=X)

if r.status_code==200:
    print('Local host responded')
    print(f'prediction result: {r.text}')

else:
    print('Recheck deploy status')
# %%
