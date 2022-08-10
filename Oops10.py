class A:
    class_var = " I am a class variable in class A"

    def __init__(self):
        self.var1 = " I am inside class A's constructor"
        self.class_var = "Instance var in class A"
        self.special = " Special "


class B(A):
    class_var = "I am in class B"

    def __init__(self):
        self.var1 = " I am inside class B's constructor"
        self.class_var = "Instance var in class B"
        super().__init__()
        print(super().class_var)


a = A()
b = B()

print(b.special)
print(b.class_var)