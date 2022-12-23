# def add(*args):
#     sum = 0
#     for no in args:
#         sum += no
#     print(sum)
#
# add(5,6,7,2,49,1)

def calc(n, **kwargs):
    print(kwargs)
    n+= kwargs["add"]
    n+= kwargs["multiply"]
    print(n)

calc(2, add=5, multiply=15)

class Car:

    def __init__(self, **kw):
        self.make = kw["make"]
        self.model = kw["model"]

mycar = Car(make="Mustang", model="GT-800")
print(mycar.model)