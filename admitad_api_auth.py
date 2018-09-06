#admitad
#идентификатор 5969e46166212aa7204d81b8f69c17
#секретный ключ 1e864c069de6bac42e746488be3579
#закодированные заголовок авторизации NTk2OWU0NjE2NjIxMmFhNzIwNGQ4MWI4ZjY5YzE3OjFlODY0YzA2OWRlNmJhYzQyZTc0NjQ4OGJlMzU3OQ==
#http://export.admitad.com/ru/webmaster/websites/178044/coupons/export/?website=178044&filter=1&code=0402c3ac4a&keyword=&region=RU&only_my=on&user=webmaster2015&format=csv&v=4

#direct
#ID: 9841e1fb3b0e411f8cfe6844ff68bd9f
#Пароль: 79dad2e2b94b4c79a97c2ec8c833271f
#Callback URL: https://oauth.yandex.ru/verification_code
#access_token=AQAAAAAaB6PfAAUWO9_FMrRYnkIQn_k2PAjHNIE&token_type=bearer&expires_in=31536000


import requests
import json
import time
from base64 import b64encode

client_id='5969e46166212aa7204d81b8f69c17'
client_secret='1e864c069de6bac42e746488be3579'
hdata = client_id + ':' + client_secret
data_b64_encoded = b64encode(hdata.encode()).decode()

print(data_b64_encoded)

headers = {'Authorization':'Basic NTk2OWU0NjE2NjIxMmFhNzIwNGQ4MWI4ZjY5YzE3OjFlODY0YzA2OWRlNmJhYzQyZTc0NjQ4OGJlMzU3OQ==', 'Content-Type':'application/x-www-form-urlencoded;charset=UTF-8'}
data = {'grant_type':'client_credentials', 'client_id':'5969e46166212aa7204d81b8f69c17', 'scope':'advcampaigns banners websites'}

r = requests.post('https://api.admitad.com/token/', data = data, headers = headers)

#file = open('refresh_data.txt', 'w')
#file.

access_token = r2['access_token']
refresh_token = r2['refresh_token']
expires_in = r2['expires_in']
get_token_time = time.time()
refresh_time = get_token_time + expires_in


print(r.text)
print(access_token)
print(refresh_time)

