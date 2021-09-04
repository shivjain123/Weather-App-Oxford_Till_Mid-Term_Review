# -*- coding: utf-8 -*-

import pandas as pd
import requests as req
import plotly_express as px
import tkinter as tk
import time

r = req.get('https://api.openweathermap.org/data/2.5/onecall?lat=23.599&lon=77.4126&dt=1586468027&&appid=1bddb27de6fe856d12b27e8e9e0d2e1c').json()
#print(r)

#Current
sunrise_c = time.strftime('%I:%M:%S', time.gmtime(r['current']['sunrise'] - 21600))
sunset_c = time.strftime('%I:%M:%S', time.gmtime(r['current']['sunset'] - 21600))
feels_like_c = int(r["current"]["feels_like"]-273.15)
temp_c = int(r["current"]["temp"]-273.15)
uvi_c = r["current"]["uvi"]
visible_c = r["current"]["visibility"]
pressure_c = r["current"]["pressure"]
humid_c = r["current"]["humidity"]
description_c = r["current"]["weather"][0]["description"]
w_speed_c = r["current"]["wind_speed"]
deg_c = r["current"]["wind_deg"]
timezone_c = r["timezone"]

#Daily
sunrise_d = time.strftime('%I:%M:%S', time.gmtime(r["daily"][0]["sunrise"] - 21600))
sunset_d = time.strftime('%I:%M:%S', time.gmtime(r["daily"][0]["sunset"] - 21600))

moon_rise = r["daily"][0]["moonrise"]
moon_set = r["daily"][0]["moonset"]

feels_like_day = int(r["daily"][0]["feels_like"]["day"]-273.15)
feels_like_night = int(r["daily"][0]["feels_like"]["night"]-273.15)

temp_d_day = int(r["daily"][0]["temp"]["day"]-273.15)
temp_d_night = int(r["daily"][0]["temp"]["night"]-273.15)

rain = r["daily"][0]["rain"]
uvi_d = r["daily"][0]["uvi"]
pressure_d = r["daily"][0]["pressure"]
humid_d = r["daily"][0]["humidity"]
description_d = r["daily"][0]["weather"][0]["description"]
w_speed_d = r["daily"][0]["wind_speed"]
deg_d = r["daily"][0]["wind_deg"]

#loop for Current Deg
if deg_c in [0, 360]:
  deg_c = "Towards North"
elif deg_c > 0 and deg_c < 90:
  deg_c = "Towards North-East"
elif deg_c == 90:
  deg_c = "Towards East"
elif deg_c > 90 and deg_c < 180:
  deg_c = "Towards South-East"
elif deg_c == 180:
  deg_c = "Towards South"
elif deg_c > 180 and deg_c < 270:
  deg_c = "Towards South-West"
elif deg_c == 270:
  deg_c = "Towards West"
elif deg_c > 270 and deg_c < 360:
  deg_c = "Towards North-West"

#loop for Daily Deg
if deg_d in [0, 360]:
  deg_d = "Towards North"
elif deg_d > 0 and deg_d < 90:
  deg_d = "Towards North-East"
elif deg_d == 90:
  deg_d = "Towards East"
elif deg_d > 90 and deg_d < 180:
  deg_d = "Towards South-East"
elif deg_d == 180:
  deg_d = "Towards South"
elif deg_d > 180 and deg_d < 270:
  deg_d = "Towards South-West"
elif deg_d == 270:
  deg_d = "Towards West"
elif deg_d > 270 and deg_d < 360:
  deg_d = "Towards North-West"

weather_list = [temp_c, feels_like_c, description_c, timezone_c, sunrise_c, sunset_c, pressure_c, humid_c, uvi_c, visible_c, 
                 deg_c, w_speed_c, temp_d_day,temp_d_night, feels_like_day, feels_like_night,description_d, sunrise_d, sunset_d, 
                 moon_rise, moon_set, pressure_d, humid_d, rain, uvi_d,deg_d, w_speed_d]

#print(weather_list)

df = pd.DataFrame([weather_list], columns =['temp_c', 'feels_like_c', 'description_c', 'timezone_c', 'sunrise_c', 'sunset_c', 
'pressure_c', 'humid_c', 'uvi_c', 'visible_c', 'deg_c', 'w_speed_c', 'temp_d_day','temp_d_night', 'feels_like_day',
'feels_like_night','description_d', 'sunrise_d', 'sunset_d', 'moon_rise','moon_set','pressure_d', 'humid_d', 'rain','uvi_d','deg_d', 'w_speed_d'])

print(df)
