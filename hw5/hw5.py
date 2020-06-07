'''
15-110 Homework 5
Name:       Jonathan Schwartz
Andrew ID:  jschwar4
'''

import pathlib
path = str(pathlib.Path(__file__).parent.absolute()) + "\\"

################################################################################

''' #1 - Counting with MapReduce '''

def mapFileToCount(s):
    s.splitlines()    #splitting at new lines
    temp = s.split()  #splitting at spaces

    capital_count = 0
    #loop through all words and tally capital first letters
    for word in temp:
        ascii_code = ord(word[0])
        if (ascii_code > 64) and (ascii_code < 91):
            capital_count += 1
    return capital_count

def reduceCountsToTotal(counts):
    sum = 0
    for i in counts:
        sum += i
    return sum

################################################################################

''' Test Functions '''

def readFile(filename):
    f = open(path + filename, "r")
    text = f.read()
    f.close()
    return text

def testMapFileToCount():
    print("Testing mapFileToCount()...", end="")
    assert(mapFileToCount(readFile("data/chapter1.txt")) == 148)
    assert(mapFileToCount(readFile("data/chapter2.txt")) == 214)
    assert(mapFileToCount(readFile("data/chapter12.txt")) == 212)
    print("... done!")

def testReduceCountsToTotal():
    print("Testing reduceCountsToTotal()...", end="")
    assert(reduceCountsToTotal([148, 214, 212]) == 574)
    assert(reduceCountsToTotal([148]) == 148)
    assert(reduceCountsToTotal([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 55)
    print("... done!")

# This code is a bit complicated, but you aren't responsible for it.
def mapWrapper(filename):
    print("Running Mapper on:", filename)
    return [("count", mapFileToCount(readFile(filename)))]
def reduceWrapper(tup):
    print("Running Reducer on:", tup[1])
    return reduceCountsToTotal(tup[1])

def testCountMapReduce():
    print("Testing countMapReduce()...", end="")

    # We'll test the whole process on the entire text of Alice in Wonderland
    # (courtesy of Project Gutenberg), split across 12 chapters in 12 files.

    # Get all the files
    files = [ "data/chapter" + str(n) + ".txt" for n in range(1, 13) ]

    # Run MapReduce on them
    from mapreduce import SimpleMapReduce
    process = SimpleMapReduce(mapWrapper, reduceWrapper)
    result = process(files)[0]

    # Check the result
    assert(result == 2586)

    # Want to see the work the MapReduce process did? Run this file, then click
    # 'Terminate' on the shell. The grey text that shows up at the bottom was
    # printed by the process!
    print("... done!")

def testAll():
    testMapFileToCount()
    testReduceCountsToTotal()
    testCountMapReduce()

if __name__ == '__main__':
    testAll()
