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


emp1 = Employee("Parth", 555, "Developer")
emp2 = Employee("Ravi", 111, "Designer")

emp1.change_leaves(5)

print(emp1.no_of_leaves)
print(emp2.no_of_leaves)
print(emp2.display())
