import requests

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/onecall"
api_key = ""        # ENTER YOUR API KEY

weather_params = {
    "lat": 20.395220,                              #  ENTER YOUR LATTITUDE
    "lon": 78.128067,                              #  ENTER YOUR LONGITUDE
    "appid": api_key,
    "exclude": "current, minutely, daily"
}

will_rain = False

response = requests.get(OWM_Endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()
weather_slice = weather_data["hourly"][:12]
print(weather_slice)
for hour_data in weather_slice:
    condition_code = hour_data["weather"][0]["id"]
    print(condition_code)
    if condition_code < 700:
        will_rain = True
if will_rain:
    with smtplib.SMTP("smtp.gmail.com", 535) as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr="MY_EMAIL",          # ENTER YOUR EMAIL ID
            to_addrs="MY_PASSWORD",        # ENTER YOUR EMAIL ID PASSWORD
            msg=f"Subject:RAINING \n\n TODAYS RAINING KEEP UMBRELLA WITH YOU."
        )


