# f = open("DemoText.txt", "rt")

# READ FILE

'''print(1,f.readline())
print(2,f.readline())
print(3,f.readline())'''


'''for line in f:
    print(line)
'''

'''content = f.read()
print(content)'''

'''content = f.read(5)
print(content)'''

# WRITE FILE

'''f = open("writeDemo.txt", "w")
a = f.write("This section contains a Python reference documentation.\n")
print(a)'''

'''f = open("writeDemo.txt", "a")
a = f.write("\nThis section contains a Python reference documentation.")
print(a)'''

# READ AND WRITE
'''f = open("writeDemo.txt","r+")

f.write("Hello")

print(f.read())'''

# f = open("DemoText.txt")

'''print(f.tell())
print(f.readline())
print(f.tell())
print(f.readline())
print(f.tell())'''

'''print(f.readline())
print(f.seek(0))
print(f.readline())'''

# f.close()


with open("writeDemo.txt") as f :
    a = f.read()

    print(a)
