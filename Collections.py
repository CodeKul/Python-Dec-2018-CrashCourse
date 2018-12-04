# String

# str = 'Codekul'
# int = 100
# float = 10.20
# print("Value: %d, %s, %f"%(int, str, float))
# print("Value: {}, {}, {}".format(int, str, float))

# str = '''"Codekul"- The Gurukul for Coders!'''

# print(str)

# List

myList = [1,2,3,4,5,6,7,8,9, 10.20, 'Codekul', "The Gurukul for Coders"]
print(myList)

myList.append(55555)
print(myList)

myList.remove(10.20)
print(myList)

myList.sort()
print(myList)

myList.insert(10,"Ten")
print(myList)

myList[10] = 'Nine'
print(myList)

for data in myList:
    print(data)

for element in myList:
    if not isinstance(element, str):
        myList.remove(element)

i = 0
while i < len(myList):
    if isinstance(myList[i], int):
        myList.remove(myList[i])
    else:
        i += 1

print(myList)



# Tuple

t1 = (1,2,3,4,5, 'Codekul')
# t1[0] = 10

print(t1)

for t in t1:
    print(t)

# Dictionary

myDict = {'one': 1,'two':2,'three':3, 4: 'four'}
print(myDict['one'])
print(myDict['two'])
print(myDict['three'])
print(myDict[4])

myInfo = {'Name': 'Jyoti', 'Address': 'Pune', 'Phone': 1234567890}
print(myInfo['Name'])
print(myInfo['Address'])
print(myInfo['Phone'])