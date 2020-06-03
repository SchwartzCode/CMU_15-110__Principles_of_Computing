'''
15-110 Homework 2
Name:       Jonathan Schwartz
Andrew ID:  jschwar4
'''

import math as m

################################################################################

''' #1 - pythagoreanChecker(a, b, c) '''

def pythagoreanChecker(a, b, c):
    if (a**2 + b**2) == c**2 or (b**2 + c**2) == a**2 or (a**2 + c**2) == b**2:
        return True
    else:
        return False


''' #2 - printPrimeFactors(x) '''

def printPrimeFactors(x):
    while x > 1:
        for i in range(2,(x+1)):
            if (x%i == 0):
                print(i)
                x = x//i
                i=2
                break
    return


''' #3 - Testing and Debugging '''


def isEven(x):
    if x % 2 == 0:
        return True
    else:
        return False

def battleTextGenerator(person1, person2):
    text = "TONIGHT: " + person1 + " VS " + person2
    return text

def makeAdditionString(x, y):
    return str(x) + " + " + str(y) + " = " + str(x + y)



''' #4 - factorial(x) '''

def factorial(x):
    prod = 1
    while (x>1):
        prod = prod*x
        x = x-1
    return prod


''' #5 - printTriangle(n) '''

def printTriangle(n):
    middle = n//2 + 1
    maxWidth = n//2 + 1

    for i in range(n+1):
        if (i < middle):
            line = "*" * i
        elif i == middle:
            line = "*" * maxWidth
        else:
            line = "*" * (maxWidth - abs(i - middle))
        print(line)
    return


''' #6 - getMiddleSentence(s) '''

def getMiddleSentence(s):
    s = s.replace("!", ".")
    s = s.replace("?", ".")

    sentNum = s.count(".")

    if (sentNum == 3):
        index1 = s.find(".")
        index2 = s.find(".", index1+1)

        output = s[index1+2:index2]
        return output
    else:
        return "Improper structure"




################################################################################
''' Test Functions '''

def testPythagoreanChecker():
    print("Testing pythagoreanChecker()...", end="")
    assert(pythagoreanChecker(3, 4, 5) == True)
    assert(pythagoreanChecker(4, 3, 5) == True)
    assert(pythagoreanChecker(4, 5, 3) == True)
    assert(pythagoreanChecker(16, 63, 65) == True)
    assert(pythagoreanChecker(3, 4, 6) == False)
    assert(pythagoreanChecker(10, 10, 10) == False)
    assert(pythagoreanChecker(1, 1, 2) == False)
    print("... done!")

def testPrintPrimeFactors():
    print("Testing printPrimeFactors()...")
    printPrimeFactors(70) # 2, 5, 7
    print("---")
    printPrimeFactors(12) # 2, 2, 3
    print("---")
    printPrimeFactors(16) # 2, 2, 2, 2
    print("---")
    printPrimeFactors(36) # 2, 2, 3, 3
    print("---")
    printPrimeFactors(3289) # 11, 13, 23
    print("... check your output to see if it looks correct!")

def testIsEven():
    print("Testing isEven()...", end="")
    assert(isEven(12) == True)
    assert(isEven(15) == False)
    assert(isEven(0) == True)
    assert(isEven(-5) == False)
    assert(isEven(-8) == True)
    print("... done!")

def testBattleTextGenerator():
    print("Testing battleTextGenerator()...", end="")
    assert(battleTextGenerator("The Rock", "Hulk Hogan") == "TONIGHT: The Rock VS Hulk Hogan")
    assert(battleTextGenerator("CMU Tartans", "MIT Beavers") == "TONIGHT: CMU Tartans VS MIT Beavers")
    assert(battleTextGenerator("Avatar Aang", "Avatar Korra") == "TONIGHT: Avatar Aang VS Avatar Korra")
    print("... done!")

def testMakeAdditionString():
    print("Testing makeAdditionString()...", end="")
    assert(makeAdditionString(3, 4) == "3 + 4 = 7")
    assert(makeAdditionString(6, 6) == "6 + 6 = 12")
    assert(makeAdditionString(-2, 200) == "-2 + 200 = 198")
    print("... done!")

def testFactorial():
    print("Testing factorial()...", end="")
    assert(factorial(1) == 1)
    assert(factorial(2) == 2)
    assert(factorial(3) == 6)
    assert(factorial(4) == 24)
    assert(factorial(5) == 120)
    assert(factorial(6) == 720)
    assert(factorial(10) == 3628800)
    assert(factorial(0) == 1)
    print("... done!")

def testPrintTriangle():
    print("Testing printTriangle()...")
    printTriangle(1)
    print("---")
    printTriangle(3)
    print("---")
    printTriangle(5)
    print("---")
    printTriangle(7)
    print("---")
    printTriangle(9)
    print("... check your output to see if it looks correct!")

def testGetMiddleSentence():
    print("Testing getMiddleSentence()...", end="")
    assert(getMiddleSentence("One. Two. Three.") == "Two")
    assert(getMiddleSentence("One. One two! One two three?") == "One two")
    assert(getMiddleSentence("You've got to ask yourself a question. Do I feel lucky? Well, do ya, punk?") == "Do I feel lucky")
    assert(getMiddleSentence("This! Is a very? Improper sentence.") == "Is a very")
    assert(getMiddleSentence("Don't worry. We'll make sure every sentence? ends with punctuation.") == "We'll make sure every sentence")
    assert(getMiddleSentence("This doesn't have three sentences!") == "Improper structure")
    assert(getMiddleSentence("This. Is. Way way way! Too? Many! Sentences.") == "Improper structure")
    print("... done!")

def testAll():
    testPythagoreanChecker()
    testPrintPrimeFactors()
    testIsEven()
    testBattleTextGenerator()
    testMakeAdditionString()
    testFactorial()
    testPrintTriangle()
    testGetMiddleSentence()

testAll()
