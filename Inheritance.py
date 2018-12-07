class Polygon:
    sides = []
    def __init__(self,n):
        super().__init__()
        self.n = n
    def inputSides(self):
        for n in range(self.n):
            side = input("Enter {} side: ".format(n))
            self.sides.append(side)
    def displaySides(self):
        for side in self.sides:
            print(side)

# p = Polygon(5)
# p.inputSides()
# p.displaySides()

class Triangle(Polygon):
    def __init__(self):
        super().__init__(3)

# t = Triangle()
# t.inputSides()
# t.displaySides()

class Rectangle(Polygon):
    def __init__(self):
        super().__init__(4)
    def inputSides(self):
        length = input("Enter Length: ")
        breadth = input("Enter Breadth: ")
        for n in range(self.n):
            if n % 2 == 0:
                self.sides.append(length)
            else:
                self.sides.append(breadth)

# r = Rectangle()
# r.inputSides()
# r.displaySides()

class Square(Rectangle):
    # def __init__(self):
    #     super().__init__()
    def inputSides(self):
        side = input("Enter side: ")
        for n in range(self.n):
            self.sides.append(side)

s = Square()
s.inputSides()
s.displaySides()

