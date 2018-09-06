# This Python file uses the following encoding: utf-8

#ID: 9841e1fb3b0e411f8cfe6844ff68bd9f
#Пароль: 79dad2e2b94b4c79a97c2ec8c833271f
#Callback URL: https://oauth.yandex.ru/verification_code
#https://oauth.yandex.ru/authorize?response_type=token&client_id=9841e1fb3b0e411f8cfe6844ff68bd9f
#curl -k -H "Authorization: Bearer AQAAAAAaB6PfAAUWO9_FMrRYnkIQn_k2PAjHNIE" -d '{"method":"get","params":{"SelectionCriteria":{},"FieldNames":["Id","Name"]}}' https://api-sandbox.direct.yandex.com/json/v5/campaigns
#https://api.direct.yandex.com/json/v5/reports
#https://api.direct.yandex.com/json/v5/keywordbids
#https://api.direct.yandex.com/json/v5/keywords


#ID: bc932f67b5ab4ad6aecd323c6bef8731
#Пароль: d7b22557594b46a7a9a5d1520b99b6c9
#token: AQAAAAAaB6b0AAUsztQbPOdymkXroJSYLCmo6iQ
#login: admitad-2f0cabf73bde2e7b088c4a


import json
import requests
import csv


#Получаем данные из яндекса

token = 'AQAAAAAaB6b0AAUsztQbPOdymkXroJSYLCmo6iQ'
login = 'admitad-2f0cabf73bde2e7b088c4a'
url = 'https://api.direct.yandex.com/json/v5/reports'
headers = {'Authorization' : 'Bearer ' + token, 'Accept-Language' : 'ru', 'Client-Login' : login, 'Content-Type' : 'application/json; charset=utf-8'}
data = json.dumps({
    "params": {
      "SelectionCriteria": {
        "Filter": [{
          "Field": "CampaignId",
          "Operator": "IN",
          "Values": [ "36648094", ]
        }]
      },
      "FieldNames": [ "CriteriaId", "Clicks", "Cost" ],
      "ReportName": "Actual Data",
      "ReportType": "CRITERIA_PERFORMANCE_REPORT",
      "DateRangeType": "LAST_30_DAYS",
      "Format": "TSV",
      "IncludeVAT": "YES",
      "IncludeDiscount": "YES"
    }
  })

r = requests.post(url, headers = headers, data = data)

#with open('data_file.json', 'w') as write_file:
#    json.dump(r.json(), write_file)

print(r)
print(r.text)
#print(r.json())


