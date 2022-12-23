import requests
from datetime import datetime
import smtplib
import time

Email = "196330307024.jeet.gaikwad@gmail.com"
Password = "jng@0905"

MY_LAT = 20.593683 # Your latitude
MY_LONG = 78.962883 # Your longitude


def iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    #Your position is within +5 or -5 degrees of the ISS position.
    if MY_LAT-5 <= iss_latitude <= MY_LAT+5 and MY_LONG-5 <= iss_longitude <= MY_LONG+5:
        return  True

def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now().hour

    if time_now >=sunset or time_now <= sunrise:
        return True

# BONUS: run the code every 60 seconds.
while True:
    time.sleep(60)
    if iss_overhead() and is_night():
        connection = smtplib.SMTP("smtp.gmail.com")
        connection.starttls()
        connection.login(Email, Password)
        connection.sendmail(
            from_addr=Email,
            to_addrs=Email,
            msg="Subject:Look Up\n\nThe ISS is above you in the sky"
        )