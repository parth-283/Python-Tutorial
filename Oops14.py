class Employee:
    def __init__(self, f_name, l_name):
        self.f_name = f_name
        self.l_name = l_name

    def explain(self):
        return f"This Employee is {self.f_name} {self.l_name}"

    @property
    def email(self):
        if self.f_name is None or self.l_name is None:
            return "Email is not set. Please set it using setter"
        return f"{self.f_name}.{self.l_name}@gmail.com"

    @email.setter
    def email(self, string):
        names = string.split("@")[0]
        self.f_name = names.split(".")[0]
        self.l_name = names.split(".")[1]

    @email.deleter
    def email(self):
        self.f_name = None
        self.l_name = None


emp1 = Employee("Parth", "Kathiriya")

print(emp1.explain())
print(emp1.email)
emp1.email = "Hello.Hii@gmail.com"
print(emp1.email)
del emp1.email
print(emp1.email)
