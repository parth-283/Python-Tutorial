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

    # Class Methods As Alternative Constructors
    @classmethod
    def from_str(cls, string):
        return cls(*string.split("-"))

    # Static Methods
    @staticmethod
    def print_good(string):
        print("This is Good " + string)


emp1 = Employee("Parth", 555, "Developer")
emp2 = Employee("Ravi", 111, "Designer")
# Class Methods As Alternative Constructors
emp3 = Employee.from_str("Danny-102-Coder")

emp1.change_leaves(5)

print(emp1.no_of_leaves)
print(emp2.no_of_leaves)
print(emp1.display())
print(emp2.display())

# Class Methods As Alternative Constructors
print(emp3.display())

# Static Methods
emp3.print_good("Hello")
