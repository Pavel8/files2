class table:
    def __init__(self, tvar, velikost, material):
        self.tvar = tvar
        self.velikost = velikost
        self.material = material

t1 = table("oval", "L", "dub")
t2 = table( tvar = "obdelnik", velikost = "M", material = "briza")

print(t1.velikost)
print(t2.tvar)


class city:
    def __init__(self, name:str, region, country, people:int, ZIP):
        self.name = name
        self.region = region
        self.country = country
        self.people = people
        self.ZIP = ZIP

    def __str__(self):
        return f"name:{self.name}, region:{self.region}, country:{self.country}, people:{self.people}, ZIP:{self.ZIP}"

    @staticmethod
    def city_create():
        name = input(f"Pridej jmeno:")
        region = input("Pridej region: ")
        country = input("Pridej country: ")
        people = int(input("Pridej pocet obyvatel: "))  # Convert to integer
        ZIP = input("Pridej ZIP kod: ")
        return city(name,region,country,people,ZIP)

c2 = city.city_create()

c1 = city("Brno","JM_kraj","CZ", 400000, [60200, 63800])


print (c1)


