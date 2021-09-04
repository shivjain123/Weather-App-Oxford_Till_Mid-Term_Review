# -*- coding: utf-8 -*-

import pandas as pd
import requests as req
import plotly.express as px
import tkinter as tk
import time

r = req.get('http://api.openweathermap.org/data/2.5/forecast?q=Bhopal&APPID=1bddb27de6fe856d12b27e8e9e0d2e1c').json()
#print(r)

if r["cod"] != "404":
    name = r["city"]["name"]
    timezone = r["city"]["timezone"]
    country = r["city"]["country"]
    population = r["city"]["population"]
    lat = r["city"]["coord"]["lat"]
    lon = r["city"]["coord"]["lon"]
    sunrise = time.strftime('%I:%M:%S', time.gmtime(r['city']['sunrise'] - 21600))
    sunset = time.strftime('%I:%M:%S', time.gmtime(r['city']['sunset'] - 21600))
    date_time = r["list"][0]["dt_txt"]
    temp = r["list"][0]["main"]["temp"]-273.15
    pressure = r["list"][0]["main"]["pressure"]
    humid = r["list"][0]["main"]["humidity"]
    sea_level = r["list"][0]["main"]["sea_level"]
    ground_level = r["list"][0]["main"]["grnd_level"]
    rain_in_3h = r["list"][0]["rain"]['3h']
    description = r["list"][0]["weather"][0]["description"]
    w_speed = r["list"][0]["wind"]["speed"]
    deg = r["list"][0]["wind"]["deg"]
    gust = r["list"][0]["wind"]["gust"]

    if deg in [0, 360]:
        deg = "Towards North"
    elif deg > 0 and deg < 90:
      deg = "Towards North-East"
    elif deg == 90:
      deg = "Towards East"
    elif deg > 90 and deg < 180:
      deg = "Towards South-East"
    elif deg == 180:
      deg = "Towards South"
    elif deg > 180 and deg < 270:
      deg = "Towards South-West"
    elif deg == 270:
      deg = "Towards West"
    elif deg > 270 and deg < 360:
      deg = "Towards North-West"

else:
    print("Data Unavailable")

weather_list = [name, country, timezone, population, lat, lon, sunrise, sunset, date_time, description, temp, sea_level, ground_level, rain_in_3h, pressure, humid, deg, w_speed, gust]

#print(weather_list)

df = pd.DataFrame([weather_list], columns = ['name', 'country', 'timezone', 'population', 'lat', 'lon', 'sunrise', 'sunset', 'date_time', 'description', 'temp', 'sea_level', 'ground_level', 'rain_in_3h', 'pressure', 'humid', 'deg', 'w_speed', 'gust'])
#print(df)