def my_function():
    print('This is my function')

my_function()

def my_function_with_param(data):
    print(data)

my_function_with_param('Codekul')

def my_function_with_default_param(data='Codekul'):
    print(data)

my_function_with_default_param('MeLayer')

def changeTheData(value):
    print(value)
    value = 100
    print('Inside call: {}'.format(value))

value = 10
print('Before call: {}'.format(value))
changeTheData(value)
print('After call: {}'.format(value))

def chageTheList(myList):
    # myList.append(100)
    myList = [6,7,8,9,0]
    print('Inside call: {}'.format(myList))

myList = [1,2,3,4,5]
print('Before call: {}'.format(myList))
chageTheList(myList)
print('After call: {}'.format(myList))

def function_with_returning_value():
    return [12,34,56,89]

value = function_with_returning_value()
print(value)

def calculate_area_of_circle(radius):
    return 3.14*(radius**2)

radius = 33
area = calculate_area_of_circle(radius)
print('Area of circle with radius {} is: {}'.format(radius, area))

def function1(data):
    print('Inside function1')
    print('function1: {}'.format(data))

def function2(myFunction, data):
    print('Inside function2')
    print('Before calling myFunction')
    myFunction(data)
    print('After calling myFunction')

print('Before calling function2')
function2(function1, 10)
print('After calling function2')
