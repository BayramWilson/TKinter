def add(*args):
    c = 0
    for n in args:
        c = c + n
    return c

solution = add(5,5,5,5,5)
print(solution)



def calculate(n, **kwargs):
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)

calculate(2, add= 3, multiply = 5)

class Car:

    def __init__(self, **kw):
        self.make = kw.get("make")
        self.model = kw.get("type")

my_car = Car(make="Toyota", type="Civic Type R")
print(my_car)