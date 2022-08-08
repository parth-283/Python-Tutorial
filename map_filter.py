'''numbers = ["2", "56", "32"]
numbers = list(map(int, numbers))'''


#for i in range(len(numbers)):
#   numbers[i] = int(numbers[i])

# numbers[2] = numbers[2] + 1
# print(numbers[2])

# def sq(a):
#     return a * a
#

# Map Function
'''num = [2, 3, 5, 6, 9, 8, 5, 5, 5, 6, 9]
square = list(map(lambda x:x*x, num))
print(square)'''


'''def square(a):
    return a*a
def cube(a):
    return a*a*a

func = [square, cube]
# num = [ 2,3,4,5,6,9,5,23,6,52,55]

for i in range(5):
    val = list(map(lambda x:x(i),func))
    print(val)'''


#Filter Function

'''list_1 = [1,2,3,4,5,6,7,8,9,5,5,6,5]

def is_greater(num):
    return num > 5

gr_then_5 = list(filter(is_greater,list_1))
print(gr_then_5)'''

# Reduce Function

from functools import reduce
list1 = [1,2,3,5,6,8,9,4,6,4,5]
'''num = 0
for i in list1:
    num = num + i

print(num)'''


num = reduce(lambda x,y:x+y, list1)
print(num)