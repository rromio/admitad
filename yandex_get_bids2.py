# This Python file uses the following encoding: utf-8

#webmaster12.1
#ID: 9841e1fb3b0e411f8cfe6844ff68bd9f
#Пароль: 79dad2e2b94b4c79a97c2ec8c833271f
#Callback URL: https://oauth.yandex.ru/verification_code
#https://oauth.yandex.ru/authorize?response_type=token&client_id=9841e1fb3b0e411f8cfe6844ff68bd9f
#curl -k -H "Authorization: Bearer AQAAAAAaB6PfAAUWO9_FMrRYnkIQn_k2PAjHNIE" -d '{"method":"get","params":{"SelectionCriteria":{},"FieldNames":["Id","Name"]}}' https://api-sandbox.direct.yandex.com/json/v5/campaigns
#https://api.direct.yandex.com/json/v5/reports
#https://api.direct.yandex.com/json/v5/keywordbids
#https://api.direct.yandex.com/json/v5/keywords

#admitad-2f0cabf73bde2e7b088c4a
#ID: bc932f67b5ab4ad6aecd323c6bef8731
#Пароль: d7b22557594b46a7a9a5d1520b99b6c9
#token: AQAAAAAaB6b0AAUsztQbPOdymkXroJSYLCmo6iQ
#login: admitad-2f0cabf73bde2e7b088c4a
#https://oauth.yandex.ru/verification_code#access_token=AQAAAAAaB6b0AAUsztQbPOdymkXroJSYLCmo6iQ&token_type=bearer&expires_in=30927971

#/root/projects/admitad/



import json
import requests
import csv



#Обрабатываем файл с рекомендуемыми ставками
with open('/root/projects/admitad/optimum2.csv', 'r') as optimum_file:
    optimum_price_list = list(csv.reader(optimum_file))

keywordids_list = []

for line in optimum_price_list:
    keywordids_list.append(int(line[0]))



#Получаем токен из файла
with open('/root/projects/admitad/tokens.txt', 'r') as tokens_file:
    data_tokens = eval(tokens_file.read())

token = data_tokens['access_token2']



#Получаем данные из яндекса
login = 'webmaster12.1'
url = 'https://api.direct.yandex.com/json/v5/keywordbids'
headers = {'Authorization' : 'Bearer ' + token, 'Accept-Language' : 'ru', 'Client-Login' : login, 'Content-Type' : 'application/json; charset=utf-8'}
data = json.dumps({
    "method": "get",
    "params": {"SelectionCriteria": {"KeywordIds": keywordids_list}, "FieldNames": ["KeywordId", ], "SearchFieldNames": ["Bid", "AuctionBids"]},
})

r = requests.post(url, headers = headers, data = data)

#with open('data_file.json', 'w') as write_file:
#    json.dump(r.json(), write_file)

#print(r)
#print(r.text)
#print(r.json())



#Обрабатываем ставки
data_bids = r.json()

#with open('data_file.json', 'r') as read_file:
#    data = json.load(read_file)

bid_list = []

def get_optimum_price(id):
    for item in optimum_price_list:
        if int(item[0]) == id:
            return int(item[1])


for i in data_bids['result']['KeywordBids']:
    try:
        keywordid = i['KeywordId']
        search = i['Search']
        actual_bid = i['Search']['Bid']
        auction_bid_items = i['Search']['AuctionBids']['AuctionBidItems']
        new_bid = 0
        optimum_price = get_optimum_price(keywordid)
        if optimum_price != None:
            for i2 in auction_bid_items:
                if i2['Price'] <= optimum_price:
                    if actual_bid < i2['Bid']:
                        new_bid = i2['Bid']
                        bid_list.append({'SearchBid': new_bid, 'KeywordId': keywordid})
                        break
                    elif actual_bid > i2['Bid']:
                        new_bid = i2['Bid']
                        bid_list.append({'SearchBid': new_bid, 'KeywordId': keywordid})
                        break
                    else:
                        break
            print('KeywordId:' + str(keywordid) + ', Optimum:' + str(optimum_price) + ', New Bid:' + str(new_bid) + '. ' + str(search))
    except:
        continue

print('Sending bids: ' + str(bid_list))



#Отправляем ставки
if bid_list != []:
    data_set = json.dumps(
        {
            "method" : "set",
            "params" : {
                "KeywordBids" : bid_list

            }

        }
    )
    r_set = requests.post(url, headers = headers, data = data_set)
    with open('/root/projects/admitad/log2.txt', 'a') as write_file:
        write_file.write(str(r_set) + r_set.text + '\n')
        print(r_set)
        print(r_set.text)
        print(r_set.json())
else:
    with open('/root/projects/admitad/log2.txt', 'a') as write_file:
        write_file.write('No changes\n')
        print('No changes')



#Загрузка в pandas выгрузки ключевых слов df1 = pandas.DataFrame([{'KeywordId': 123123, 'Bid': 400000}, {'KeywordId': 123124, 'Bid': 400000}])
#Сворачивание в json списка ключевых слов со ставками df1.to_dict('records')
# Кодирование тела запроса в JSON jsonBody = json.dumps(body, ensure_ascii=False).encode('utf8')

