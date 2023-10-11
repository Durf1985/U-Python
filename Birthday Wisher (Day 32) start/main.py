import random

import pandas
import datetime as dt
import smtplib
import os

birth_day_list = pandas.read_csv("birthdays.csv").to_dict(orient="records")
print(birth_day_list)
now = dt.datetime.now()
today = (7, 13)

files = os.listdir("letter_templates")
print(files)

for record in birth_day_list:
    if (record["month"], record["day"]) == today:
        with open(f"letter_templates/{random.choice(files)}") as file:
            text = file.readlines()
            text = ''.join([line.replace('[NAME]', record["name"]) for line in text])
            print(text)

        with smtplib.SMTP("smtp.gmail.com") as connection:
            user = "Durf19851@gmail.com"
            password = "cjtpnqgrwaxjwzgz"
            connection.starttls()
            connection.login(user=user, password=password)
            connection.sendmail(from_addr=user, to_addrs=user, msg=f"subject:Happy Birthday \n\n {text}")
