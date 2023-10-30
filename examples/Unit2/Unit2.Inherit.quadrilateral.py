class quadriLateral:
    def __init__(self, a, b, c, d):
        self.side1 = a
        self.side2 = b
        self.side3 = c
        self.side4 = d

    def perimeter(self):
        p = self.side1 + self.side2 + self.side3 + self.side4
        print("perimeter=", p)

q1 = quadriLateral(7, 5, 6, 4)
q1.perimeter()

#design a rectangle class based upon the quadriLateral class
class rectangle(quadriLateral):
    def __init__(self, a, b):
        super().__init__(a, b, a, b)
        #The __init__() method forwards the parameters to the constructor of its base
        # (quadrilateral) class using the super() function

    def area(self):
        a = self.side1 * self.side2
        print("area of rectangle=", a)

r1 = rectangle(10, 20)
r1.perimeter() #60
r1.area() #200

#define the square class which inherits the rectangle class.
# The area() method is overridden to implement the formula
# for the area of the square as the square of its sides.
class square(rectangle):
    def __init__(self, a):
        super().__init__(a, a)

    def area(self):
        a = pow(self.side1, 2)
        print('Area of Square: ', a)

s = square(10)
s.area()  # output: Area of Square:  100
s.perimeter() #40