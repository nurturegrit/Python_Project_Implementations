import pandas

# Finding common integers in file1 and file2

data1 = pandas.read_csv("file1.txt", header=None).squeeze()
data2 = pandas.read_csv("file2.txt", header=None).squeeze()

list1 = data1.tolist()
list2 = data2.tolist()
common_elements = [int(num) for num in list1 if num in list2 ]
print(common_elements)