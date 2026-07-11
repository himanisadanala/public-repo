# ###api's###
# import requests
# city=input("enter city:")
# url=f"https://wttr.in/{city}?format=j1"
# response=requests.get(url)

# data=response.json()
# temp=data["current_condition"][0]["temp_C"]
# humidity=data["current_condition"][0]["humidity"]
# wind=data["current_condition"][0]["windspeedKmph"]
# condition=data["current_condition"][0]["weatherDesc"][0]["value"]

# print("temperature:",temp,"C")
# print("humidity:",humidity,"%")
# print("wind:",wind,"kmph")
# print("weather:",condition)

# hourly=data["weather"][0]["hourly"]
# for hour in hourly:
#     print(
#         f"time:{hour['time']} |"
#         f"temp:{hour['tempC']}C |"
#         f"humidity:{hour['humidity']}% |"
#         f"weather:{hour['weatherDesc'][0]['value']}"
#     )

import requests
city = input("enter city:")
url = f"https://wttr.in/{city}?format=j1"
response = requests.get(url)
data = response.json()
current = data["current_condition"][0]
print("\n--------------Current weather--------------")
print("city:",city)
print("temperature:",current["temp_C"],"C")
print("humidity:",current["humidity"],"%")
print("wind speed:",current["windspeedKmph"],"km/h")
print("weather:",current["weatherDesc"][0]["value"])
print("----------------Hourly Forecast------------------")
hourly = data["weather"][0]["hourly"]
for hour in hourly:
    print(
        f"Time: {hour['time']}|"
        f"Temp: {hour['tempC']}C|"
        f"Humidity: {hour['humidity']}%|"
        f"weather: {hour['weatherDesc'][0]['value']}")