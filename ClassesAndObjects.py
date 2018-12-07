class Student:
    name = ""
    rno = 0
    marks = 0.0

    # def __init__(self):
    #     self.name = ""
    #     self.rno = 0
    #     self.marks = 0.0

    def __init__(self, name, rno, marks):
        self.name = name
        self.rno = rno
        self.marks = marks
        print('__init__')

    def display(self):
        print('Name: {}'.format(self.name))
        print('Roll no.: {}'.format(self.rno))
        print('Marks: {}'.format(self.marks))


# stu1 = Student('Jyoti', 1, 90)
# stu1.display()


class Car:
    
    # def __init__(self):
    #     self.speed = 0
    #     self.hp = 0
    #     self.weight = 0
    #     self.color = ''
    #     self.model = ''

    def __init__(self, speed, hp, weight, color, model):
        self.speed = speed
        self.hp = hp
        self.weight = weight
        self.color = color
        self.model = model

    def accelerate(self):
        self.speed += 1
        print('Moving forward... with speed {}'.format(self.speed))

    def applyBreaks(self):
        self.speed -= 1
        print('Stopping the car at speed {}'.format(self.speed))

    def printModel(self):
        print('Model: {}'.format(self.model))
    
    def changeColor(self, newColor):
        print('Changing color from {} to {}'.format(self.color, newColor))
        self.color = newColor

    def printCarDetails(self):
        print('Speed: {}'.format(self.speed))
        print('HP: {}'.format(self.hp))
        print('Weight: {}'.format(self.weight))
        print('Color: {}'.format(self.color))
        self.printModel()


c1 = Car(0, 50, 100, 'Red', 'Verna')
c1.accelerate()
c1.accelerate()
c1.applyBreaks()

c1.printCarDetails()

c1.changeColor('White')

c1.printCarDetails()
