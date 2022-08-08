from email.policy import EmailPolicy


class Employee:
    no_of_leaves = 8
    pass


emp1 = Employee()
emp2 = Employee()

emp1.name = "Parth"
emp1.salary = 10000
emp1.role = "Instructor"
emp2.name = "Ravi"
emp2.salary = 20000
emp2.role = "Developer"

print(emp1.no_of_leaves)
emp1.no_of_leaves = 9
print(emp1.__dict__)
print(emp2.__dict__)
print(Employee.__dict__)
print(emp1.no_of_leaves)
