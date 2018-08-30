import json
import requests
import csv


#Обрабатываем файл с рекомендуемыми ставками

with open('optimum.csv', 'r') as optimum_file:
    optimum_price_list = list(csv.reader(optimum_file))

keywordids_list = []

for line in optimum_price_list:
    keywordids_list.append(int(line[0]))

print(keywordids_list)