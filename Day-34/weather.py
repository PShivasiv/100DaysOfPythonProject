import requests
from twilio.rest import Client 

api_key = "OWN APi"
OWM_endpoint = "https://api.openweathermap.org/data/2.5/forecast"

account_sid = "own account"
auth_token = "Own Token"



parameter = {
    "lat":28.704060,
    "lon":28.704060,
    "appid":api_key,
    "cnt":4,
    
}

response = requests.get(url=OWM_endpoint,params=parameter)
response.raise_for_status()
weather_data = response.json()

# weather_id = weather_data["list"][0]["weather"][0]["id"] This is to take the single data from the json file but we want to 3 days data

for hour_date in weather_data["list"]:
    condition_code = hour_date["weather"][0]["id"]


    if int(condition_code) < 700:
        will_rain = True

#     )
if will_rain:
    client = Client(account_sid, auth_token)

    message = client.messages \
        .create(
        from_="+14155238886",
        body="It's going to rain today . Remember to bring an umbrella",
        to="+919873810930",
    )
print(message.status)

























