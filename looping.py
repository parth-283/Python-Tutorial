list1 = ["Apple","Apricots","Avocado","Banana","Blackberries","Blackcurrant","Blueberries","Breadfruit","Cantaloupe","Carambola","Cherimoya","Cherries","Clementine","Coconut Meat","Cranberries","Custard-Apple","Date Fruit","Durian","Elderberries","Feijoa","Figs","Gooseberries","Grapefruit"]

# For Loop

# for item in list1 :
    # print(item)

# item1 = ["My", "Your", 1, 6, 3, 5, 85, 45, 10, 7]
#
# for item in item1:
#     if str(item).isnumeric() and item > 6 :
#         print(item)

# While Loop break and continue

# i = 0
#
# while (i<20):
#     i+=1
#     if (i == 4):
#         continue
#     if(i == 11):
#         break
#
#     print(i, end=" ")

# exercise
no_guess = 9
i = 0
no = 15
while (i <= 9):
    user = int(input("Enter your Guess... "))
    if(user < no):
        print("Your guess is Less then number")
    elif(user > no):
        print("Your guess is Greater then number")
    elif (user == no):
        print("Your guess is Right",i)
        break
    i += 1
    if(i == 9):
        print(" ...Game Over... ")
        break


# exercise
n = 5
user = input("enter 0 or 1 number... ")
print(user,bool(user))

if True == bool(user):
    for i in range(0, n):
        for j in range(0, i + 1):
            print("* ", end="")
        print()
elif False == bool(user):
    for i in range(n + 1, 0, -1):
        for j in range(0, i - 1):
            print("* ", end="")
        print()
else:
    print("Please Enter 0 or 1..")