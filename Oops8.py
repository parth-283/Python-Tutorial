# Multilevel Inheritance
'''class Dad:
    basketball = 1


class Son(Dad):
    dance = 1

    def isDance(self):
        return f"Yes I dance {self.dance} no of times"


class GrandSon(Son):
    dance = 6

    def isDance(self):
        return f"Yes I dance very awesome {self.dance} no of times"


darry = Dad()
larry = Son()
harry = GrandSon()

print(harry.isDance())
print(harry.basketball)

'''
# exercise
class Electronic:
    Category = {"fen": 2, "Phone": 5, "Light": 10, "Pocket": 15}


class Pocket(Electronic):
    def pocket_print(self):
        return f"Pocket Gadgets is {self.Category['Pocket']}"


class Phone(Pocket):
    def phone_print(self):
        return f"Phone Gadgets is {self.Category['Phone']}"


electronic_gadget = Electronic()
pocket_gadget = Pocket()
Phone_gadget = Phone()

print(Phone_gadget.pocket_print())
print(Phone_gadget.phone_print())
