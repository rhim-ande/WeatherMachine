import requests
import pprint
import json
import os
import pandas as pd
import sqlalchemy as db
from sqlalchemy import create_engine 


option_input = input("Enter one weather option: \n 1. Forecast \n 2. Realtime Weather \n 3. History \n ")


if option_input == "1":
    city_input = input("Enter your city name: ")
    #days_input = input("Enter number of days for your forecast: ")

    url = 'http://api.weatherapi.com/v1/forecast.json'
    querystring = {"q":{city_input},"days":"3"}
    headers = {
	"key": "fdab0fe0b1d1492c889224703220707"
    }
    response = requests.get(url, headers=headers, params=querystring)

    weather_data = response.json()['forecast']

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

    weather_dataframe = pd.DataFrame(list(zip(empty_list1, empty_list2, empty_list3, empty_list4, empty_list5)),
               columns =['Date', 'MaxTemp', 'MinTemp', 'AvgTemp', 'AvgHumidity'])


    engine = db.create_engine('sqlite:///forecast_weather.db')
    weather_dataframe.to_sql('weather_info', con=engine, if_exists='replace', index=False)
    query_result = engine.execute("SELECT * FROM weather_info;").fetchall()
    df = pd.DataFrame(query_result)

    df.columns = ["Date", "MaxTemp", "MinTemp", "AvgTemp", "AvgHumidity"]

    print(df)



if option_input == "2":
    city_input = input("Enter your city name: ")
    url = "http://api.weatherapi.com/v1/current.json"
    querystring = {"q":{city_input}}
    headers = {
        "key": "fdab0fe0b1d1492c889224703220707"

    }
    response = requests.get(url, headers=headers, params=querystring)
    realtime_data = response.json()['current']
    empty_list1 = []
    empty_list2 = []
    empty_list3 = []
    empty_list1.append(realtime_data['last_updated'])
    empty_list2.append(realtime_data['temp_f'])
    empty_list3.append(realtime_data['condition']['text'])

    weather_dataframe = pd.DataFrame(list(zip(empty_list1, empty_list2, empty_list3)))


    engine = db.create_engine('sqlite:///realtime_weather.db')
    weather_dataframe.to_sql('realtime_info', con=engine, if_exists='replace', index=False)
    query_result = engine.execute("SELECT * FROM realtime_info;").fetchall()
    df = pd.DataFrame(query_result)

    df.columns = ["Time Updated", "Temp_F", "Condition"]

    print(df)



          

if option_input == "3":
    city_input = input("Enter your city name: ")
    date_input = input("Enter date in the format yyyy-mm-dd (upto last 7 days): ")
    url = "http://api.weatherapi.com/v1/history.json"
    querystring = {"q":{city_input},"dt":{date_input},"lang":"en"}
    headers = {
	    "key": "fdab0fe0b1d1492c889224703220707"
    }
    response = requests.get(url, headers=headers, params=querystring)
    weather_data = response.json()['forecast']

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

    weather_dataframe = pd.DataFrame(list(zip(empty_list1, empty_list2, empty_list3, empty_list4, empty_list5)),
               columns =['Date', 'MaxTemp', 'MinTemp', 'AvgTemp', 'AvgHumidity'])


    engine = db.create_engine('sqlite:///forecast_weather.db')
    weather_dataframe.to_sql('weather_info', con=engine, if_exists='replace', index=False)
    query_result = engine.execute("SELECT * FROM weather_info;").fetchall()
    df = pd.DataFrame(query_result)

    df.columns = ["Date", "MaxTemp", "MinTemp", "AvgTemp", "AvgHumidity"]

    print(df)

