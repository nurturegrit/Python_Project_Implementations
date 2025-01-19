import smtplib

import pandas
import datetime
import random
def get_birthdays(filepath):
    data = pandas.read_csv(filepath)
    return {(data_row["month"], data_row["day"]): data_row for index, data_row in data.iterrows()}

birthdays = get_birthdays("birthdays.csv")
today_tuple = (datetime.datetime.now().month, datetime.datetime.now().day)

try:
    birthday_person = birthdays[today_tuple]
    email = "sumitjaidka786@gmail.com"
    letter = open(f"letter_templates/letter_{random.randint(1,3)}.txt")
    content = letter.read()
    letter.close()
    content = content.replace("[NAME]", birthday_person["name"])
    server = smtplib.SMTP("smtp.gmail.com", port=587)
    server.starttls()
    server.login(email, "gsai chlq kmav iali")
    server.sendmail(to_addrs=birthday_person["email"], from_addr=email, msg="Subject:Happy Birthday!!\n\n"
                                                                            f"{content}")
    server.quit()
except KeyError:
    print("No Birthday for Anyone in the file")