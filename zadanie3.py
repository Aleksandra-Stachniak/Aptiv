#!/usr/bin/python
# -*- coding: utf-8 -*-

import csv
import os
import requests

def weather_forecast():
    api_key = '4732bf1c26dcc24e67d1e563115666dd'
    city = 'Kraków'
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={api_key}&units=metric"
    req = requests.get(url)
    data = req.json()
    filtered_forecast = filter(lambda forecast: forecast["main"]["temp_min"] < 10, data["list"])
    formatted_forecast = map(lambda forecast: {"Data": forecast['dt_txt'], "Temp min": forecast['main']['temp_min']}, filtered_forecast)

    return list(formatted_forecast)


def save_to_csv(data, filename):
    fieldnames = ["Data", "Temp min"]

    with open(filename, 'w', newline="") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)


if __name__ == "__main__":
    filename = input("Podaj nazwę pliku CSV: ")

    while os.path.isfile(filename):
        print(f"Plik '{filename}' już istnieje. Wybierz inną nazwę pliku.")
        filename = input("Podaj nazwę pliku CSV: ")

    new_weather_forecast = weather_forecast()
    save_to_csv(new_weather_forecast, filename)
    print("Dane zostały zapisane do pliku CSV.")