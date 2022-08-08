'''def func1():
    print("HELLO")


func2 = func1

del func1

func2()
'''


def dec1(func1):
    def func2():
        print("Executing now")
        func1()
        print("Executed")

    return func2


@dec1
def parth():
    print("Boy")


# parth = dec1(parth)
parth()
