'''def func1():
    print("HELLO")


func2 = func1

del func1

func2()
'''


def dec1(func1):
    def nowexec1():
        print("Executing now")
        func1()
        print("Executed")

    return nowexec1


@dec1
def parth():
    print("Boy")


# parth = dec1(parth)
parth()
