import smtplib

email = "sumitjaidka786@gmail.com"
password = "gsai chlq kmav iali"
connection = smtplib.SMTP("smtp.gmail.com", port=587)
connection.starttls()
connection.login(email, password)
connection.sendmail(from_addr=email, to_addrs="sumitatcultivatewill@yahoo.com", msg="Subject:Python Mail"
                                                                                    "\n\nHello")
connection.quit()