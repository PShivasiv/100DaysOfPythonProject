import requests
import datetime as dt
import smtplib
import time

LATITUDE = 28.704060
LONGITUDE = 77.102493

my_email = "siv23shiva@gmail.com"
password = "YOUR PASSWORD"


def is_iss_overhead():
    reponse = requests.get(url="http://api.open-notify.org/iss-now.json")  # This get code fetch the date from the ending url of the website and return the response
    reponse.raise_for_status()

    data = reponse.json()

    longitude = float(data["iss_position"]["longitude"])
    latitude = float(data["iss_position"]["latitude"])

    if LATITUDE-5 <= latitude <= LATITUDE+5 and LONGITUDE-5 <= longitude <= LONGITUDE+5:
        return True

def is_night():
    perameter = {
        "let":LATITUDE,
        "lng":LONGITUDE,
        "formatted":0,

    }

    response = requests.get(url="https://api.sunrise-sunset.org/json",params=perameter)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split(":")[0])
    sunset = int(data["results"]["sunset"].split(":")[0])


    time_now = dt.now().hour

    if time_now >= sunset or time_now <= sunrise:
        return True
    
while True:   
    time.sleep(60) 
    if is_iss_overhead() and is_night():
        connection = smtplib.SMTP("smtp.gmail.com")
        connection.starttls()
        connection.login(user=my_email,password=password)
        connection.sendmail(from_addr=my_email,to_addrs=my_email,msg="Subject:LOOKUP....!\n\n This ISS is above you in the sky")
