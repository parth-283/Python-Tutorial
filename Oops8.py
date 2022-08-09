# Multilevel Inheritance
class Dad:
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