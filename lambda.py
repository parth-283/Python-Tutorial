# Lambda function or Anonymous function

# Lambda Function
'''minus = lambda x ,y : x-y
print(minus(9,4))'''

# Normal Function
'''def minus(x,y):
    return x-y
print(minus(9,4))'''


# Sort function
'''def a_first(a):
    return a[1]'''

a_first = lambda a:a[1]

a = [[1, 4], [5, 9], [6, 5]]

a.sort(key=a_first)
print(a)
