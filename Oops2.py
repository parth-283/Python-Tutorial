class Employee:
    no_of_leaves = 8

    def display(self):
        return f"Employee => Name is {self.name}, Salary is {self.salary}, role is {self.role} "


emp1 = Employee()
emp2 = Employee()

emp1.name = "Parth"
emp1.salary = 455
emp1.role = "Instructor"

emp2.name = "Ravi"
emp2.salary = 450
emp2.role = "Developer"
emp2.no_of_leaves = 15

print(emp1.display())
print(emp2.display())


# Constructor
class Student:
    division = "MCA"

    def __init__(self, name, roll):
        self.name = name
        self.roll = roll

    def display(self):
        print("Roll : %d \nName : %s \nDivision : %s \n" % (self.roll, self.name, self.division))


stu1 = Student("Parth", 1)
stu2 = Student("Akash", 2)

stu1.display()
stu2.display()
