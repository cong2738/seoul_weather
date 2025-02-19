import requests
import csv
from datetime import datetime
import os

API_KEY ="1d070a9b64263edd97eb0c9d54534111"
CITY = "Seoul"
URL = f"http://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric"

response = requests.get(URL)
data = response.json()
# print(data)

temp = data["main"]["temp"]
humidity = data["main"]["humidity"]
description = data["weather"][0]["description"]
timezone = datetime.now().strftime("%y-%m-%d %H:%M:%S")

# print(temp,humidity,description,timezone)

csv_filename = "seoul_weather.csv"
header = ["timezone", "temp", "humidity", "weather"]

file_exist = os.path.isfile(csv_filename)

# mode = "a" -> if not file -> create
# if file -> wirte 
with open(csv_filename, "a") as file:
    writer = csv.writer(file)

    if not file_exist: #파일이 없으면 헤더를 쓴다(파일 최초상태)
        writer.writerow(header)
    
    writer.writerow([timezone,temp,humidity,description])

    print("csv 저장 완료!!")
