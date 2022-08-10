class A:
    def met(self, name):
        print(f"This is a method from class A call to {name}")


class B(A):
    def met(self, name):
        print(f"This is a method from class B call to {name}")


class C(A):
    def met(self, name):
        print(f"This is a method from class C call to {name}")


class D(B, C):
    def met(self, name):
        print(f"This is a method from class D call to {name}")


a = A()
b = B()
c = C()
d = D()

print(a.met('a'))
print(b.met('b'))
print(c.met('c'))
print(d.met('d'))
