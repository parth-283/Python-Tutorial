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


# Inheritance
class Programmer(Employee):

    def __init__(self, name, salary, role, languages):
        self.name = name
        self.salary = salary
        self.role = role
        self.languages = languages

    def print_prog(self):
        return f"Programmer => Name is {self.name}, Salary is {self.salary}, role is {self.role}, Languages are {self.languages} "


class Player:
    no_of_games = 4

    def __init__(self, name, game):
        self.name = name
        self.game = game

    def print_games(self):
        return f"Player => Name is {self.name}, Games is {self.game}"


# Multiple Inheritance
class CoolProgrammer(Employee, Player):
    language = 'c++'

    def print_language(self):
        print(self.language)


emp1 = Employee("Parth", 555, "Developer")
emp2 = Employee("Ravi", 111, "Designer")
# Class Methods As Alternative Constructors
emp3 = Employee.from_str("Danny-102-Coder")
# Inheritance
pro1 = Programmer("Rakesh", 466, "Programmer", ['Python', 'React'])
pro2 = Programmer("Jay", 562, "Programmer", ['JavaScript'])

player1 = Player("Dishant", ['judo', 'karate', 'kusti'])

cool1 = CoolProgrammer("Karan", 900, "CoolProgrammer")

print(pro1.print_prog())
print(pro2.print_prog())

print(player1.print_games())

# Multiple Inheritance
print(cool1.print_language())
