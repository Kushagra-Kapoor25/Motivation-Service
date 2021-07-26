import os
import smtplib
import datetime as dt
from random import choice
from dotenv import load_dotenv
load_dotenv()

MY_EMAIL = os.getenv("EMAIL")
PASSWORD = os.getenv("PASSWORD")

now = dt.datetime.now()
day = now.weekday()

if day == 0:
    with open("quotes.txt") as file:
        all_quotes = file.readlines()
        quote = choice(all_quotes)
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs="rajkhanna512@yahoo.com",
            msg=f"Subject:Monday Motivation\n\n{quote}"
        )
