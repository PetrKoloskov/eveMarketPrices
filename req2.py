import requests
import json
import pandas as pd
type_id = [34, 54535]
region_id = 10000002
system_id = 30000142

#получаем цены по региону
def getFilteredList(region_id, system_id, type_id):
    params = dict(type_id=str(type_id), order_type='sell')
    url = 'https://esi.evetech.net/v1/markets/'+str(region_id)+'/orders/'
    rec = requests.get(url, params=params)
    #фильтруем ордера по системе в выбранном регионе
    return list(filter(lambda x: x['system_id'] == system_id, json.loads(rec.text)))

minPriceList=[]
for id in type_id:
    filteredList=getFilteredList(region_id, system_id, id)

#ищет минимальный ордер на покупку
    min_price=1000000000
    for item in filteredList:
        if(float(item['price'])<min_price):
            min_price = float(item['price'])
    minPriceList.append(min_price)

#читает выбранные id и выводит id и названия
df = pd.read_excel('sample.xlsx')

#выводим предмет и его минимальную цену на продажу
result=[]
for index, row in df.iterrows():
    if int(row[0]) in type_id:
        result.append(row[1])
for i in range(len(result)):
    print(result[i],' - ',minPriceList[i])




