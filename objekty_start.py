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