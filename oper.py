import json
import requests
from base64 import b64encode



#Функция обновления токенов в файле
def rewrite_tokens():
    data_tokens['access_token1'] = new_access_token
    data_tokens['refresh_token1'] = new_refresh_token
    with open('tokens.txt', 'w') as write_file:
        write_file.write(str(data_tokens))



#Получаем закодированную строку
client_id='bc932f67b5ab4ad6aecd323c6bef8731'
client_secret='d7b22557594b46a7a9a5d1520b99b6c9'
hdata = client_id + ':' + client_secret
data_b64_encoded = b64encode(hdata.encode()).decode()



#Получаем токен и рефреш токены из файла
with open('tokens.txt', 'r') as tokens_file:
    data_tokens = eval(tokens_file.read())

refresh_token = data_tokens['refresh_token1']
access_token = data_tokens['access_token1']



#Получаем токен и рефреш токен из Яндекса
url = 'https://oauth.yandex.ru/token'
headers = {'Authorization' : 'Basic ' + data_b64_encoded, 'Content-Type' : 'application/x-www-form-urlencoded'}
data = {"grant_type": 'refresh_token', 'refresh_token': refresh_token}

r = requests.post(url, headers = headers, data=data)

print(r)
print(r.text)
print(r.json())

print(r.json()['access_token'])
print(r.json()['refresh_token'])

new_access_token = r.json()['access_token']
new_refresh_token = r.json()['refresh_token']



#Если токены обновились, вызываем обновление файла
if new_access_token != access_token:
    rewrite_tokens()
elif new_refresh_token != refresh_token:
    rewrite_tokens()



