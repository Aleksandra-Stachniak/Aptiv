#!/usr/bin/python
# -*- coding: utf-8 -*-

import requests
import argparse

def weather_forecast():
    parser = argparse.ArgumentParser()
    parser.add_argument("--min-temp", type=float, help="Minimalna temperatura (w stopniach Celsjusza)", required=True)
    args = parser.parse_args()

    try:
        min_temp = float(args.min_temp)
    except ValueError:
        print("Błąd: Podana temperatura nie jest wartością liczbową")
        return

    api_key = '4732bf1c26dcc24e67d1e563115666dd'
    city = 'Kraków'
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={api_key}&units=metric"
    req = requests.get(url)
    data = req.json()
    forecast_list = data["list"]

    filtered_forecast = filter(lambda forecast: forecast["main"]["temp_min"] < min_temp, forecast_list)
    formatted_forecast = map(lambda forecast: f"Date: {forecast['dt_txt']}, TempMin: {forecast['main']['temp_min']}", filtered_forecast)

    for forecast in formatted_forecast:
        print(forecast)


weather_forecast()