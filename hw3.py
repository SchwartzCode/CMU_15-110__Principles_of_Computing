'''
15-110 Homework 3
Name:       Jonathan Schwartz
Andrew ID:  jschwar4
'''
import numpy as np

################################################################################

''' #1 - hiddenMessage(s) '''

def hiddenMessage(s):
    temp = s.split(" ")
    output = ""
    for i in range(len(temp)):
        output += temp[i][i]
    return output


''' #2 - letterFrequency(s) '''

def letterFrequency(s):
    output = [0]*26
    tmp = s.lower()
    tmp.strip()
    while (len(tmp) > 0):
        pos = ord(tmp[0]) - 97
        if (pos >= 0):
            output[pos] = output[pos] + 1
        tmp = tmp[1:]
    return output


''' #3 - onlyPositive(lst) '''

def onlyPositive(lst):
    output = []
    for i in range(len(lst)):
        for j in range(len(lst[0])):
            if lst[i][j] > 0:
                output.append(lst[i][j])
    return output


''' #4 - recursiveMax(lst) '''
"""
max = lst[0]
if (len(lst) < 2):
    return max
else:
    while(len(lst) > 0):
        if (lst[0] > max):
            max = lst[0]
        lst = lst[1:]
"""

def recursiveMax(lst):
    if (len(lst) == 1):
        return lst[0]
    else:
        backMax = recursiveMax(lst[1:])
        if backMax > lst[0]:
            return backMax
        else:
            return lst[0]


''' #5 - recursiveCount(lst, item) '''

def recursiveCount(lst, item):
    if (len(lst) == 0):
        return 0
    elif (len(lst) == 1):
        if(lst[0] == item):
            return 1
        else:
            return 0
    else:
        if (lst[0] == item):
            counter = 1
        else:
            counter = 0
        counter += recursiveCount(lst[1:], item)

    return counter


################################################################################
''' Test Functions '''

def testHiddenMessage():
    print("Testing hiddenMessage()...", end="")
    assert(hiddenMessage("I'm here") == "Ie")
    assert(hiddenMessage("Come to office hours") == "Cofr")
    assert(hiddenMessage("I") == "I")
    assert(hiddenMessage("See May Day") == "Say")
    assert(hiddenMessage("Happy Very Yelp Call Yellow") == "Hello")
    assert(hiddenMessage("Hear Monday Now Paid Money") == "Howdy")
    print("... done!")

def testLetterFrequency():
    print("Testing letterFrequency()...", end="")
    assert(letterFrequency("Hello World") ==                [0,0,0,1,1,0,0,1,0,0,0,3,0,0,2,0,0,1,0,0,0,0,1,0,0,0])
    assert(letterFrequency("quick brown fox")            == [0,1,1,0,0,1,0,0,1,0,1,0,0,1,2,0,1,1,0,0,1,0,1,1,0,0])
    assert(letterFrequency("Carnegie Mellon University") == [1,0,1,0,4,0,1,0,3,0,0,2,1,3,1,0,0,2,1,1,1,1,0,0,1,0])
    assert(letterFrequency("ABCDEFGHIJKLMNOPQRSTUVWXYZ") == [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1])
    assert(letterFrequency("abcdefghijklmnopqrstuvwxyz") == [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1])
    assert(letterFrequency("") ==                           [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
    print("... done!")

def testOnlyPositive():
    print("Testing onlyPositive()...", end="")
    assert(onlyPositive([[1, 2, 3], [4, 5, 6]]) == [1, 2, 3, 4, 5, 6])
    assert(onlyPositive([[0, 1, 2], [-2, -1, 0], [10, 9, -9]]) == [1, 2, 10, 9])
    assert(onlyPositive([[-4, -3], [-2, -1]]) == [ ])
    assert(onlyPositive([[3, 4, 5]]) == [3, 4, 5])
    assert(onlyPositive([[-4], [3], [5]]) == [3, 5])
    assert(onlyPositive([[-1, 2], [-3, 4], [-5, 6]]) == [2, 4, 6])
    assert(onlyPositive([[1, 5, -3, 7, 9, -23, -45, 67]]) == [1, 5, 7, 9, 67])
    assert(onlyPositive([[-5], [-4], [-3], [-2], [-1]]) == [ ])
    assert(onlyPositive([ [0], [0] ]) == [ ])
    print("... done!")

def testRecursiveMax():
    print("Testing recursiveMax()...", end="")
    assert(recursiveMax([1, 2, 3]) == 3)
    assert(recursiveMax([2, 4, 6, 9, 10, 2, 6]) == 10)
    assert(recursiveMax([3, 4, 5]) == 5)
    assert(recursiveMax([4, 5, 1]) == 5)
    assert(recursiveMax([1,2,3,6,5,1]) == 6)
    assert(recursiveMax([67,5,3,7,9,23,45,0]) == 67)
    assert(recursiveMax(["dog","cat","bird","bear"]) == "dog")
    assert(recursiveMax(["dog","bird","elephant","bear"]) == "elephant")
    assert(recursiveMax(["mouse","cat","dog","fox"]) == "mouse")
    print("... done!")

def testRecursiveCount():
    print("Testing recursiveCount()...", end="")
    assert(recursiveCount([2, 4, 6, 8, 10], 6) == 1)
    assert(recursiveCount([4, 4, 8, 4], 4) == 3)
    assert(recursiveCount([1, 2, 3, 4], 5) == 0)
    assert(recursiveCount([9, 9, 9], 9) == 3)
    assert(recursiveCount([5, 1, 3, 7, 6, 2, 9, 8, 10], 10) == 1)
    assert(recursiveCount([5, 1, 3, 7, 6, 2, 9, 8, 10], 5) == 1)
    assert(recursiveCount([], 4) == 0)
    print("... done!")

def testAll():
    testHiddenMessage()
    testLetterFrequency()
    testOnlyPositive()
    testRecursiveMax()
    testRecursiveCount()

testAll()
