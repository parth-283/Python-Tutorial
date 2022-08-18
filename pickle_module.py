import pickle
import requests

# Pickling a Python object
# cars = ["Audi","BMW","Maruti","Ferary"]
# file = "mycar.pkl"
# fileobj = open(file,'wb')
# pickle.dump(cars,fileobj)
# fileobj.close()

# file = "mycar.pkl"
# fileobj = open(file,'rb')
# mycar = pickle.load(fileobj)
# print(mycar)
# print(type(mycar))
# fileobj.close()

# Exercise 10

# url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"
# data = requests.get(url).text
#
# l1 = data.split("\n")
# l2 = [item.split(",") for item in l1 if len(item) != 0]
#
# with open("myiris.pkl", 'wb') as f:
#     pickle.dump(l2, f)
# f.close()

# with open("myiris.pkl", 'rb') as f:
#     print(pickle.load(f))
# f.close()
