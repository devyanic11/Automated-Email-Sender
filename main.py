import smtplib
import datetime as dt
import random

my_email = "YOUR EMAIL"
password = "YOUR PASSWORD"

reciever = "RECIEVER'S EMAIL ID GOES HERE"

message = "YOUR MESSAGE GOES HERE"
subject = "YOUR SUBJECT GOES HERE" #Email might be directed to spam folder if you did not provide a subject.

with smtplib.SMTP("smtp.gmail.com", 587, timeout=360) as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(from_addr=my_email,
        to_addrs = reciever,
        msg=f"Subject:{subject}\n\n\n{message}")
    
    
# Check README.md if your email is not sent or if gmail isn't allow you to send the email via external application.
