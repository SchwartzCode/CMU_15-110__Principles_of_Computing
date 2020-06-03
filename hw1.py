'''
15-110 Homework 1
Name: Jonathan Schwartz
Andrew ID: jschwar4
'''

''' #1 - Variable Assignments '''
print("---1---")
a = 15
b = 3.14
c = "22"
d = True
a = 45
e = int(c)
f = a % e


''' #2 - Greeting Algorithm '''
print("---2---")
profK = "Kelly"
profM = "Margaret"
print("The professors are:", profK, "and", profM)


''' #3 - Math Algorithm '''
print("---3---")
x1 = 1
y1 = 1
x2 = 3
y2 = 5

diffY = y2 - y1
diffX = x2 - x1
m = diffY / diffX
print("The slope is:", m)
assert(m == 2)

''' #4 - Functions '''
print("---4---")

def fullEggCartons(eggCount):
    cartons = eggCount // 12
    return cartons

print(fullEggCartons(65), fullEggCartons(43), fullEggCartons(96))

def remainingEggs(eggCount):
    eggsLeft = eggCount % 12
    return eggsLeft

print(remainingEggs(23), remainingEggs(76), remainingEggs(51))
