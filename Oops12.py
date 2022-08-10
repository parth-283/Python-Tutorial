class Employee:
    no_of_leaves = 8

    def __init__(self, name, salary, role):
        self.name = name
        self.salary = salary
        self.role = role

    def display(self):
        return f"Employee => Name is {self.name}, Salary is {self.salary}, role is {self.role} "

    @classmethod
    def change_leaves(cls, new_leaves):
        cls.no_of_leaves = new_leaves

    # Mapping Operators to Functions
    def __add__(self, other):
        return self.salary + other.salary

    def __truediv__(self, other):
        return self.salary / other.salary

    def __repr__(self):
        return self.display() + "REPR"

    def __str__(self):
        return self.display() + "STR"


emp1 = Employee("Parth", 500, "Programmer")
emp2 = Employee("Rajesh", 85, "Cleaner")
print(emp1 + emp2)
print(emp1 / emp2)
print(repr(emp1))
print(emp1)

print(emp1.display())
