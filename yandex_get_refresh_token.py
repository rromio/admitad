import json
import requests
from base64 import b64encode

#Получеаем код: https://oauth.yandex.ru/authorize?response_type=code&client_id=9841e1fb3b0e411f8cfe6844ff68bd9f
code = 2825564

#Получаем закодированную строку
client_id='9841e1fb3b0e411f8cfe6844ff68bd9f'
client_secret='79dad2e2b94b4c79a97c2ec8c833271f'
hdata = client_id + ':' + client_secret
data_b64_encoded = b64encode(hdata.encode()).decode()

#Получаем токен и рефреш токен
url = 'https://oauth.yandex.ru/token'
headers = {'Authorization' : 'Basic ' + data_b64_encoded, 'Content-Type' : 'application/x-www-form-urlencoded'}
data = {"grant_type": 'authorization_code', 'code': str(code)}

r = requests.post(url, headers = headers, data=data)

print(r)
print(r.text)
print(r.json())



