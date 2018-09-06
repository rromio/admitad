import json
import requests
from base64 import b64encode



#Функция обновления токенов в файле
def rewrite_tokens():
    data_tokens['access_token1'] = new_access_token1
    data_tokens['refresh_token1'] = new_refresh_token1
    data_tokens['access_token2'] = new_access_token2
    data_tokens['refresh_token2'] = new_refresh_token2
    with open('/root/projects/admitad/tokens.txt', 'w') as write_file:
        write_file.write(str(data_tokens))



#Получаем токен и рефреш токены из файла
with open('/root/projects/admitad/tokens.txt', 'r') as tokens_file:
    data_tokens = eval(tokens_file.read())

refresh_token1 = data_tokens['refresh_token1']
access_token1 = data_tokens['access_token1']
refresh_token2 = data_tokens['refresh_token2']
access_token2 = data_tokens['access_token2']



#Аккаунт 1

#Получаем закодированную строку1
client_id1='bc932f67b5ab4ad6aecd323c6bef8731'
client_secret1='d7b22557594b46a7a9a5d1520b99b6c9'
hdata1 = client_id1 + ':' + client_secret1
data_b64_encoded1 = b64encode(hdata1.encode()).decode()



#Получаем токен и рефреш токен из Яндекса
url = 'https://oauth.yandex.ru/token'
headers = {'Authorization' : 'Basic ' + data_b64_encoded1, 'Content-Type' : 'application/x-www-form-urlencoded'}
data = {"grant_type": 'refresh_token', 'refresh_token': refresh_token1}

r1 = requests.post(url, headers = headers, data=data)

print(r1)
print(r1.text)
print(r1.json())

print(r1.json()['access_token'])
print(r1.json()['refresh_token'])

new_access_token1 = r1.json()['access_token']
new_refresh_token1 = r1.json()['refresh_token']



#Аккаунт 2

#Получаем закодированную строку 2
client_id2='9841e1fb3b0e411f8cfe6844ff68bd9f'
client_secret2='79dad2e2b94b4c79a97c2ec8c833271f'
hdata2 = client_id2 + ':' + client_secret2
data_b64_encoded2 = b64encode(hdata2.encode()).decode()



#Получаем токен и рефреш токен из Яндекса
url = 'https://oauth.yandex.ru/token'
headers = {'Authorization' : 'Basic ' + data_b64_encoded2, 'Content-Type' : 'application/x-www-form-urlencoded'}
data = {"grant_type": 'refresh_token', 'refresh_token': refresh_token2}

r2 = requests.post(url, headers = headers, data=data)

print(r2)
print(r2.text)
print(r2.json())

print(r2.json()['access_token'])
print(r2.json()['refresh_token'])

new_access_token2 = r2.json()['access_token']
new_refresh_token2 = r2.json()['refresh_token']



#Если токены обновились, вызываем обновление файла
if new_access_token1 != access_token1:
    rewrite_tokens()
elif new_refresh_token1 != refresh_token1:
    rewrite_tokens()
elif new_access_token2 != access_token2:
    rewrite_tokens()
elif new_refresh_token2 != refresh_token2:
    rewrite_tokens()



