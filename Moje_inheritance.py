"""
class Human:
    def __init__(self, name):
        self.name = name

    def say_hello(self):
        print(f"Hello, I am {self.name}")

class Worker(Human):
    def __init__(self, name, position,):
        Human.__init__(self, name)
        self.position = position
    def say_position(self):
        print(f"I work as {self.position}")

w1 = Worker(name = "John", position = "Ucitel")

w1.say_hello()
w1.say_position()
"""
"""
#task 2
class Passport:
    def __init__(self, name, country):
        self.name = name
        self.country = country


class ForeignPassport(Passport):
    def __init__(self, name, country, ID, visa):
        Passport.__init__(self,name, country)
        self.ID = ID
        self.visa = visa
    def vypsani(self):
        print(f"Jmeno: {self.name}, Zeme: {self.country}, Cislo dokladu: {self.ID}, Viza: {self.visa}")

Pass1 = ForeignPassport("Pavel Kadlec", "CZ", "1322456578", "USA")

print(Pass1.name, Pass1.visa)
Pass1.vypsani()

"""
#MAGIC
"""
class Num:
    def __init__(self, n):
        self.n = n

    def __eq__(self, other):
        return self.n == other.n

    def __add__(self, other):
        if type(other) is Num:
            return Num(self.n + other.n)
        return  Num(self.n + other)

    def __str__(self):
        return f"{self.n}"

n1 = Num(1)
n2 = Num(1)

def add(a, b):
    return a + b
"""
"""
class Fraction():
    def __init__(self, jmenovatel=1, citatel=0):
        self.jmenovatel = jmenovatel
        self.citatel = citatel

    def __str__(self):
        return f"{self.citatel}/{self.jmenovatel}"

    def __eq__(self, other):
        return self.jmenovatel == other.jmenovatel and self.citatel == other.citatel

    def __add__(self, other):
        j = self.jemnovatel * other.citatel
        c = self.citatel * other.jmenovatel
        return Fraction(j, c)

f1 = Fraction("2","5")
f2 = Fraction("3","8")
"""
class Fraction:
    def __init__(self, numerator=0, denominator=1):
        self.numerator = numerator
        self.denominator = denominator

    def __str__(self):
        return f"{self.numerator}/{self.denominator}"

    def __add__(self, other):
        n = self.numerator * other.denominator + other.numerator * self.denominator
        d = self.denominator * other.denominator
        return Fraction(n, d)

    def __eq__(self, o):
        return self.denominator == o.denominator and self.numerator == o.numerator

"""    @staticmethod
    def simplify_fraction(fraction):
        divisor = gcd(fraction.numerator, fraction.denominator)
        return Fraction(fraction.numerator // divisor, fraction.denominator // divisor)

"""

f1 = Fraction(1, 2)
f2 = Fraction(1, 2)

f3 = f2 + f1
print(f3) 

"""if __name__ == '__main__':
    f1 = Fraction(1, 2)
    f2 = Fraction(1, 2)

    f2 += f1
    print(f2)"""