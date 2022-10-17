import smtplib
import datetime as dt
import random

my_email = "personaldevyani@gmail.com"
password = "smtofvgsabfayhdz"

now = dt.datetime.now()
day_week = now.weekday()

if day_week == 0:
    with open("quotes.txt", "r") as data:
        lines_list = data.readlines()
        with smtplib.SMTP("smtp.gmail.com", 587, timeout=360) as connection:
            message = random.choice(lines_list)
            message.strip()
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(from_addr=my_email,
                                to_addrs="devyanichavan110@gmail.com",
                                msg=f"Subject:Monday Motivation\n\nHey Devyani!\n{message}")
