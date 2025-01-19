import smtplib
import pandas
import random
import datetime

def check_b_days(file_path):
    data = pandas.read_csv(file_path)
    # data.dropna(subset=['year', 'month', 'day'], inplace=True)
    data = data.to_dict()
    emails = []
    names = []
    # data["Date_Time"] = data.apply(lambda d: datetime.datetime(year=int(d.year), month=int(d.month), day=int(d.day)), axis=1)
    today = datetime.datetime.now()
    for index, month in data["month"].items():
        if month == today.month:
            if data["day"][index] == today.day:
                names.append(data["name"][index])
                emails.append(data["email"][index])
    return (names, emails)


# Check if today matches a birthday in the birthdays.csv
names, b_day_emails = check_b_days("birthdays.csv")
print(names, b_day_emails)
# If step 1 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
if names is not None:
    n = random.randint(1,3)
    file_path = f"letter_templates/letter_{n}.txt"
    letter = open(file_path, "r")
    template_letter = letter.read()
    letter.close()

# 4. Send the letter generated in step 3 to that person's email address.
    email = "sumitjaidka786@gmail.com"
    password = "gsai chlq kmav iali"
    server = smtplib.SMTP("smtp.gmail.com", port=587)
    server.starttls()
    server.login(email, password)
    for idx, b_email in enumerate(b_day_emails):
        l = template_letter.replace("[NAME]", names[idx])
        server.sendmail(from_addr=email, to_addrs=b_email, msg="Subject:Happy Birthday!!\n\n"
                                                              f"{l}")
    server.quit()



