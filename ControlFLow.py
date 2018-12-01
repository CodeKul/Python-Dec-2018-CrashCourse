# if
'''
if condition:
    statements
'''

a = 20

if a > 20:
    print('a is greater than 5')
    print('this is inside if')
elif a == 10:
    print('a is equal to 10')
else:
    print('a is not greater than 5 and not equal to 10')

print('this is outside if')


b = 20

if a == b:
    if a == 10:
        print('a and b are equal to 10')
    else:
        print('a and b are equal but not equal to 10')
else:
    print('a and b are not equal')


# Loops

'''
initialisation
while condition:
    statements
    incr/decr
'''

# print('Codekul')
# print('Codekul')
# print('Codekul')
# print('Codekul')
# print('Codekul')
# print('Codekul')
# print('Codekul')
# print('Codekul')
# print('Codekul')
# print('Codekul')


i = 0
while i < 10:
    if i % 2 == 0:
        print('Codekul')
    else:
        print('The Gurukul for Coders!')

    if i == 5:
        break

    i += 1

print(i)

'''
for item in collection:
    statements
'''

for ch in "Codekul":
    print(ch)