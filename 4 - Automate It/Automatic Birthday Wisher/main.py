import smtplib
import pandas
import random
import datetime
# 1. Update the birthdays.csv
def check_b_days(file_path):
    data = pandas.read_csv(file_path)
    # data.dropna(subset=['year', 'month', 'day'], inplace=True)
    data = data.to_dict()
    # data["Date_Time"] = data.apply(lambda d: datetime.datetime(year=int(d.year), month=int(d.month), day=int(d.day)), axis=1)
    today = datetime.datetime.now()
    for index, yr in data["year"].items():
        if yr == today.year:
            if data["month"][index] == today.month and data["day"][index] == today.day:
                return data["name"][index]


# 2. Check if today matches a birthday in the birthdays.csv
name = check_b_days("birthdays.csv")

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
n = random.randint(1,3)
file_path = f"letter_templates/letter_{n}.txt"
letter = open(file_path, "r")
letter = letter.read()
letter = letter.replace("[NAME]",name)

# 4. Send the letter generated in step 3 to that person's email address.
email = "sumitjaidka786@gmail.com"
password = "gsai chlq kmav iali"
server = smtplib.SMTP("smtp.gmail.com", port=587)
server.starttls()
server.login(email, password)
server.sendmail(from_addr=email, to_addrs="sumitatcultivatewill@yahoo.com", msg="Subject:Happy Birthday!!\n\n"
                                                                                f"{letter}")
server.quit()



