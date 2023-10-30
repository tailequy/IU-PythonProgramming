'''
A class can be derived from more than one superclass in Python. This is called multiple inheritance.
For example, A class Bat is derived from superclasses Mammal and WingedAnimal.
It makes sense because bat is a mammal as well as a winged animal.
class SuperClass1:
    # features of SuperClass1

class SuperClass2:
    # features of SuperClass2

class MultiDerived(SuperClass1, SuperClass2):
    # features of SuperClass1 + SuperClass2 + MultiDerived class
'''
class Mammal:
    def mammal_info(self):
        print("Mammals can give direct birth.")

class WingedAnimal:
    def winged_animal_info(self):
        print("Winged animals can flap.")

class Bat(Mammal, WingedAnimal):
    def bat_info(self):
        print("Bat can give direct birth and flap.")

# create an object of Bat class
b1 = Bat()

b1.mammal_info()
b1.winged_animal_info()
b1.bat_info()
