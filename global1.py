l = 10  # Global


def function1():
    # l = 5  # Local
    m = 8  # Local
    global l
    l = 40
    print(l, m)


print("global::", l)
function1()
