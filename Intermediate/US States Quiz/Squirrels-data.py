import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census.csv")
result = data["Primary Fur Color"].value_counts()
result = pandas.DataFrame({'Fur Color': result.index,
                           'Count': result.values})
# cinnamon = len(data[data["Primary Fur Color"] == 'Cinnamon'])
# black = len(data[data["Primary Fur Color"] == 'Black'])
# gray = len(data[data["Primary Fur Color"] == 'Gray'])
#
# result_dict = {'fur Colors' : ['Cinnamon', 'Black', 'Gray'],
#           'Count': [cinnamon, black, gray]}
# result = pandas.DataFrame(result_dict)

result.to_csv('Squirrels_Fur_colors.csv')
print(result)
