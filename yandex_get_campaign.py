#ID: 9841e1fb3b0e411f8cfe6844ff68bd9f
#Пароль: 79dad2e2b94b4c79a97c2ec8c833271f
#Callback URL: https://oauth.yandex.ru/verification_code
#https://oauth.yandex.ru/authorize?response_type=token&client_id=9841e1fb3b0e411f8cfe6844ff68bd9f
#curl -k -H "Authorization: Bearer AQAAAAAaB6PfAAUWO9_FMrRYnkIQn_k2PAjHNIE" -d '{"method":"get","params":{"SelectionCriteria":{},"FieldNames":["Id","Name"]}}' https://api-sandbox.direct.yandex.com/json/v5/campaigns
#https://api.direct.yandex.com/json/v5/reports
#https://api.direct.yandex.com/json/v5/keywordbids
#https://api.direct.yandex.com/json/v5/keywords


import json
import requests

token = 'AQAAAAAaB6b0AAUsztQbPOdymkXroJSYLCmo6iQ'
login = 'admitad-2f0cabf73bde2e7b088c4a'
url = 'https://api.direct.yandex.com/json/v5/campaigns'
headers = {'Authorization' : 'Bearer ' + token, 'Accept-Language' : 'ru', 'Client-Login' : login, 'Content-Type' : 'application/json; charset=utf-8'}
data = json.dumps({
    "method": "get",
    "params": {"SelectionCriteria":{},"FieldNames":["Id","Name"]},
})

r = requests.get(url, headers = headers, data = data)

print(r.text)
print(r.json())


#Загрузка в pandas выгрузки ключевых слов df1 = pandas.DataFrame([{'KeywordId': 123123, 'Bid': 400000}, {'KeywordId': 123124, 'Bid': 400000}])
#Сворачивание в json списка ключевых слов со ставками df1.to_dict('records')
# Кодирование тела запроса в JSON jsonBody = json.dumps(body, ensure_ascii=False).encode('utf8')