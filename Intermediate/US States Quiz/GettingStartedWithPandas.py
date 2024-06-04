# li = []
# with open("weather_data.csv",'r+') as file:
#     for line in file.readlines():
#         li.append(line.strip())
# print(li)

# import csv
#
# temps = []
# with open("weather_data.csv") as file:
#     data = csv.reader(file)
#     for row in data:
#         if row[1] == 'temp':
#             continue
#         temps.append(int(row[1]))
# print(temps)
# Too much lines for a single operation

import pandas

data = pandas.read_csv("weather_data.csv")
# print(data)
# print(type(data)) # Table is DataFrame
# print(type(data["temp"])) #Coloum is Series

#Average Temperature

# Avg_temp = data["temp"].sum() / data["temp"].shape[0]
# Avg_temp = data["temp"].mean()
# Max_temp = data["temp"].max()
# # data["temp"] == data.temp
# print(Avg_temp)

#Get Data in Rows
# print(data[data.temp == data.temp.max()])
#
# data["temp_f"] = data.temp * 9 / 5 + 32
# monday = data[data.day == "Monday"]
# print(monday)

#Creating A DataFrame From Scratch

dictionary = {'Names': ["Anna", "Montana", "Hanna"],
              'Scores': [10, 10, 9]}
records = pandas.DataFrame(dictionary)
print(records)
records.to_csv("Scores.csv")