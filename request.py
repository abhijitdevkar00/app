import requests
url = 'http://localhost:5000/predict_api'

r = requests.post(url,json={'Age':20, 'Gender':9, 'Conty':6, 'Days_Spend_In_Hospital':3})

  
print(r.json())