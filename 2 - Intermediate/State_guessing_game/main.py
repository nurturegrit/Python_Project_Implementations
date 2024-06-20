import csv
# def list_data():
#     # li_data = []
#     temp = []
#     with open('weather_data.csv','r') as file:
#         li_data = list(csv.reader(file))
#         for row in li_data[1:]:
#             temp.append(int(row[1]))
#         # for line in file.readlines():
#         #     li_data.append(list(line.strip().split(',')))
#     # print(li_data)
#     print(temp)
#
# list_data()

import pandas

data = pandas.read_csv('weather_data.csv')
print(data)
print(data['temp'])
