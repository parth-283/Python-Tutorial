import math

# WithOut FString
me = "Harry"
al = 3

a = "this is %s %s "%(me, al)
print(a)

d = "This is {} {}"
b = d.format(me,al)
print(b)

# With FString
c = f" This Is me {me} {al} {math.cos(65)}"
print(c)