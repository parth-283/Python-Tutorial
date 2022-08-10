class Employee:
    no_of_leaves = 8
    _protect_Var = 123
    __private = 896

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


emp1 = Employee("Parth", 45698, "Hello")

#  Protective Variable
print(emp1._protect_Var)

# Private Variable
print(emp1._Employee__private)
