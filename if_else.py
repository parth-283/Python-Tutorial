# var2 = 56
# var3 = int(input("Enter your number... "))
#
# if var3>var2:
#     print("Greater")
# elif var3==var2:
#     print("Equal")
# else:
#     print("Lesser")

"""
list1 = [1, 8, 9, 2, 10]
userInput = int(input("Enter your numvber..."))
"""
# With IN
"""
if userInput in list1:
    print("Yes, It's in the list { With IN }")
else:
    print("no, It's not in the list { With IN }")
"""
# With not in
"""
if userInput not in list1:
    print("no, It's not in the list { With not in }")
else:
    print("Yes, It's in the list { With not in }")
"""

"""
age = int(input("Enter your age... "))
if age < 18:
    print("You are not able to drive vehicle")
elif age > 18:
    print("You are able to drive vehicle")
else:
    print("Come for driving test")
"""


# exercise
number1 = int(input("Enter your first number... "))
operation = input("Enter your operation... ")
number2 = int(input("Enter your secound number... "))
print(number1, operation, number2)

if operation == '+' :
    if number1 == 56 and number2 == 9:
        print("ans 77")
    else:
        print("ans", number1 + number2)
    print()
elif operation == '*' :
    if number1 == 45 and number2 == 3:
        print("ans 555")
    else:
        print("ans",number1 * number2)
    print()
elif operation == '/' :
    if number1 == 56 and number2 == 6:
        print("ans 4")
    else:
        print("ans", number1 / number2)
    print()
elif operation == '-' :
    print("ans",number1 - number2)
else:
    print(" Enter valid operation")