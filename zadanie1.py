#!/usr/bin/python
# -*- coding: utf-8 -*-

import requests

def weather_forecast(api_key, city):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={api_key}&units=metric"
    req = requests.get(url)
    data = req.json()
    forecast_list = data["list"]

    filtered_forecast = filter(lambda forecast: forecast["main"]["temp_min"] < 10, forecast_list)
    formatted_forecast = map(lambda forecast: f"Date: {forecast['dt_txt']}, TempMin: {forecast['main']['temp_min']}", filtered_forecast)

    for forecast in formatted_forecast:
        print(forecast)


api_key = '4732bf1c26dcc24e67d1e563115666dd'
city = 'Kraków'

weather_forecast(api_key, city)