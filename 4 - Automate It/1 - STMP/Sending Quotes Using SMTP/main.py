import smtplib
import datetime
import random
today = datetime.datetime.now().weekday() # 0 for Monday
email = "sumitjaidka786@gmail.com"
password = "gsai chlq kmav iali"
server = smtplib.SMTP("smtp.gmail.com", port=587)
server.starttls()
server.login(email, password)
if today == 0:
    try:
        with open("quotes.txt", 'r') as quotes_file:
            quotes = list(quotes_file.readlines())
    except FileNotFoundError:
        print("File Not Found.")
    finally:
        quote = random.choice(quotes)
        server.sendmail(to_addrs="sumitatcultivatewill@gmail.com", from_addr=email, msg="Subject:Quote Of The Day\n\n"
                                                                                    f"{quote}")