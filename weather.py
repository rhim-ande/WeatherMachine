import requests
import pprint
import json
import os
import pandas as pd
import sqlalchemy as db
from sqlalchemy import create_engine 

city_input = input("Enter your city name: ")
days_input = input("Enter number of days for your forecast: ")

url = 'http://api.weatherapi.com/v1/forecast.json'

querystring = {"q":{city_input},"days":{days_input}}

headers = {
	"key": "fdab0fe0b1d1492c889224703220707"
}

response = requests.get(url, headers=headers, params=querystring)

weather_data = response.json()['forecast']

#print(weather_data['forecast'])
#pprint.pprint(weather_data['forecast'])

empty_list1 = []
empty_list2 = []
empty_list3 = []
empty_list4 = []
empty_list5 = []
data_store = weather_data['forecastday']
for data_access in data_store:
  date = data_access['date']
  max_temp = data_access['day']['maxtemp_f']
  min_temp = data_access['day']['mintemp_f']
  avg_hum = data_access['day']['avghumidity']
  avg_temp = data_access['day']['avgtemp_f']
  empty_list1.append(date)
  empty_list2.append(max_temp)
  empty_list3.append(min_temp)
  empty_list4.append(avg_temp)
  empty_list5.append(avg_hum)

subs_dataframe = pd.DataFrame(list(zip(empty_list1, empty_list2, empty_list3, empty_list4, empty_list5)),
               columns =['Date', 'MaxTemp', 'MinTemp', 'AvgTemp', 'AvgHumidity'])

print(subs_dataframe)


