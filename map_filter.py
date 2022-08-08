numbers = ["2", "56", "32"]
numbers = list(map(int, numbers))


#for i in range(len(numbers)):
#   numbers[i] = int(numbers[i])

numbers[2] = numbers[2] + 1
# print(numbers[2])

# def sq(a):
#     return a * a
#

# Map Function
num = [2, 3, 5, 6, 9, 8, 5, 5, 5, 6, 9]
square = list(map(lambda x:x*x, num))
print(square)
