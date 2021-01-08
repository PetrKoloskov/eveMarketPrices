import requests
import json
import pandas as pd
type_id = 54535
region_id = 10000002
system_id = 30000142

#получаем цены по региону
params = dict(type_id=str(type_id), order_type='sell')
url = 'https://esi.evetech.net/v1/markets/'+str(region_id)+'/orders/'
rec = requests.get(url, params=params)
'''
jsonList = rec.text
data = json.loads(jsonList)
filteredList = filter(lambda x: x['system_id'] == system_id, data)
filteredList = list(filteredList)
'''
#фильтруем ордера по системе в выбранном регионе
filteredList = list(filter(lambda x: x['system_id'] == system_id, json.loads(rec.text)))

#ищет минимальный ордер на покупку
min_price=1000000000
for item in filteredList:
    if(float(item['price'])<min_price):
        min_price = float(item['price'])
print(min_price)

#читает выбранные id и выводит id и названия
top_players = pd.read_excel('sample.xlsx')
df = top_players
idList=[34, 54535]
result=[]
for index, row in df.iterrows():
    if int(row[0]) in idList:
        result.append(row[1])
print(result)




