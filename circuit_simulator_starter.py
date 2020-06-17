"""
15-110 Hw6 - Circuit Simulator Project
Name:       Jonathan Schwartz
AndrewID:   jscwar4
"""

project = "CircuitSim"

#### CHECK-IN 1 ####

def findMatchingParen(expr, index):
    open_paren_count = 0 #start at 1 to include parentheses at index
    close_paren_indexes = [ ] #generate empty list for indexes of close parentheses
    close_index = -1

    i = index
    unclosed_count = 0

    while i<len(expr) + 1:
        if expr[i] == "(":
            unclosed_count += 1
        elif expr[i] == ")":
            unclosed_count -= 1
        if unclosed_count == 0:
            close_index = i
            break
        i += 1

    return close_index

def getTokenBounds(expr, start):
    pos = [-1, -1]
    tempDex = start
    while(tempDex < len(expr)):
        if expr[tempDex] != " ":
            pos[0] = tempDex
            break
        else:
            tempDex += 1

    if(tempDex + 1 == len(expr)):
        pos[1] = tempDex
        return pos

    while(tempDex < len(expr)):
        if expr[tempDex] == " ":
            pos[1] = tempDex - 1
            break
        else:
            tempDex += 1

    return pos

def parseExpr(expr):
    parsed = {"value" : "",
              "children" : [] }
    expr = expr.strip()

    if expr[0] == "(" and findMatchingParen(expr, 0) == len(expr) - 1:
        parsed = parseExpr(expr[1:-1])
    elif " " not in expr:
        parsed["value"] = expr
    elif expr[:3] == "NOT":
            parsed["value"] = "NOT"
            parsed["children"] = [parseExpr(expr[3:])]
    else:
        if (expr[0] == "("):
            leftEnd = findMatchingParen(expr, 0) + 1
        else:
            leftEnd = getTokenBounds(expr, 0)[1] + 1

        left = expr[:leftEnd]

        tempExpr = expr[leftEnd:].strip()
        midEnd = getTokenBounds(tempExpr, 0)[1] + 1
        mid = tempExpr[:midEnd]

        tempExpr = tempExpr[midEnd:].strip()
        right = tempExpr

        parsed["value"] = mid
        parsed["children"] = [parseExpr(left), parseExpr(right)]


    return parsed

def validateExpr(expr):
    if not "value" in expr or not "children" in expr:
        return False
    elif expr["value"] == "NOT" and len(expr["children"]) != 1:
        return False
    elif expr["value"] == "AND" or expr["value"] == "OR" or expr["value"] == "XOR":
        if len(expr["children"]) != 2:
            return False

    if "NOT" in expr["children"]:
        return validateExpr(expr["children"])


    return True

def runProgram():
    return

#### WEEK 1 TESTS ####

def testFindMatchingParen():
    print("Testing findMatchingParen()...", end="")
    expr = "(((X) AND (NOT ((Y) OR (X)))) OR (Y))"
    assert(findMatchingParen(expr, 0) == len(expr) - 1)
    assert(findMatchingParen(expr, 1) == 28)
    assert(findMatchingParen(expr, 2) == 4)
    assert(findMatchingParen(expr, 10) == 27)
    assert(findMatchingParen(expr, 15) == 26)
    assert(findMatchingParen(expr, 16) == 18)
    assert(findMatchingParen(expr, 23) == 25)
    assert(findMatchingParen(expr, 33) == 35)
    print("... done!")

def testGetTokenBounds():
    print("Testing getTokenBounds()...", end="")
    expr = "(X AND (NOT (Y OR X))) OR Y"
    assert(getTokenBounds(expr, 1) == [1, 1])
    assert(getTokenBounds(expr, 2) == [3, 5])
    assert(getTokenBounds(expr, 8) == [8, 10])
    assert(getTokenBounds(expr, 13) == [13, 13])
    assert(getTokenBounds(expr, 14) == [15, 16])
    assert(getTokenBounds(expr, 22) == [23, 24])
    assert(getTokenBounds(expr, 26) == [26, 26])
    print("... done!")

def testParseExpr():
    print("Testing parseExpr()...", end="")
    assert(parseExpr("X") == {"value": "X", "children":[]})
    assert(parseExpr("(Y)") == {"value": "Y", "children":[]})
    assert(parseExpr("(NOT X)") == {"value": "NOT", "children":[{"value": "X", "children":[]}]})
    assert(parseExpr("(FOO AND BAR)") == {"value": "AND", "children":[{"value": "FOO", "children":[]}, {"value": "BAR", "children":[]}]})
    assert(parseExpr("(X) XOR (Y)") == {"value": "XOR", "children":[{"value": "X", "children":[]}, {"value": "Y", "children":[]}]})
    assert(parseExpr("((FOO) OR (BAR))") == {"value": "OR", "children":[{"value": "FOO", "children":[]}, {"value": "BAR", "children":[]}]})
    assert(parseExpr("(X AND (NOT (Y OR X))) OR Y") == { "value" : "OR", "children" : [
        { "value" : "AND", "children" : [
            { "value" : "X", "children" : []},
            { "value" : "NOT", "children" : [
                { "value" : "OR", "children" : [
                    { "value" : "Y", "children" : []},
                    { "value" : "X", "children" : []} ]
                } ]
            } ]
        },
        { "value" : "Y", "children" : []} ]
    })
    assert(parseExpr("X AND ((NOT (Y OR X)) OR Y)") == { "value" : "AND", "children" : [
        { "value" : "X", "children" : [] },
        { "value" : "OR", "children" : [
            { "value" : "NOT", "children" : [
                { "value" : "OR", "children" : [
                    { "value" : "Y", "children" : [] },
                    { "value" : "X", "children" : [] } ]
                } ],
            },
            { "value" : "Y", "children" : [] } ]
        } ]
    })
    print("... done!")

def testValidateExpr():
    print("Testing validateExpr()...", end="")
    assert(validateExpr({ }) == False)
    assert(validateExpr({ "value" : "X", "children" : [] }) == True)
    assert(validateExpr({ "value" : "Y", "children" : [] }) == True)
    assert(validateExpr({ "value" : "AND", "children" : [
        { "value" : "X", "children" : [] },
        { "value" : "Y", "children" : [] } ]
    }) == True)
    assert(validateExpr({ "value" : "OR", "children" : [
        { "value" : "X", "children" : [] },
        { "value" : "Y", "children" : [] } ]
    }) == True)
    assert(validateExpr({ "value" : "XOR", "children" : [
        { "value" : "FOO", "children" : [] },
        { "value" : "BAR", "children" : [] } ]
    }) == True)
    assert(validateExpr({ "value" : "NOT", "children" : [
        { "value" : "X", "children" : [] } ]
    }) == True)
    assert(validateExpr({ "value" : "OR", "children" : [
        { "value" : "AND", "children" : [
            { "value" : "X", "children" : [] },
            { "value" : "OR", "children" : [
                { "value" : "NOT", "children" : [
                    { "value" : "Y", "children" : [] } ]
                },
                { "value" : "Y", "children" : [] } ]
            } ]
        },
        { "value" : "Y", "children" : [] } ]
    }) == True)

    assert(validateExpr({ "value" : "NOT", "children" : [
        { "value" : "X", "children" : [] },
        { "value" : "Y", "children" : [] } ]
    }) == False)
    assert(validateExpr({ "value" : "AND", "children": [
        { "value" : "X", "children" : [] } ]
    }) == False)
    print("... done!")



def week1Tests():
    testFindMatchingParen()
    testGetTokenBounds()
    testParseExpr()
    testValidateExpr()

week1Tests()
runProgram()

#### CHECK-IN 2 ####

def getLeaves(t):
    return

def generateAllInputs(n):
    return

def evalTree(t, inputs):
    return

def makeTruthTable(tree):
    return

#### WEEK 2 TESTS ####

def testGetLeaves():
    print("Testing getLeaves()...", end="")
    assert(getLeaves({ "value" : "X", "children" : [] }) == [ "X" ])
    assert(getLeaves({ "value" : "Y", "children" : [] }) == [ "Y" ])
    assert(getLeaves({ "value" : "AND", "children" : [
        { "value" : "X", "children" : [] },
        { "value" : "Y", "children" : [] } ]
    }) == [ "X", "Y" ])
    assert(getLeaves({ "value" : "OR", "children" : [
        { "value" : "Y", "children" : [] },
        { "value" : "X", "children" : [] } ]
    }) == [ "X", "Y" ])
    assert(getLeaves({ "value" : "XOR", "children" : [
        { "value" : "FOO", "children" : [] },
        { "value" : "BAR", "children" : [] } ]
    }) == [ "BAR", "FOO" ])
    assert(getLeaves({ "value" : "NOT", "children" : [
        { "value" : "Z", "children" : [] } ]
    }) == [ "Z" ])
    assert(getLeaves({ "value" : "OR", "children" : [
        { "value" : "AND", "children" : [
            { "value" : "X", "children" : [] },
            { "value" : "OR", "children" : [
                { "value" : "NOT", "children" : [
                    { "value" : "Y", "children" : [] } ]
                },
                { "value" : "Y", "children" : [] } ]
            } ]
        },
        { "value" : "Y", "children" : [] } ]
    }) == [ "X", "Y" ])
    assert(getLeaves({ "value" : "OR", "children" : [
        { "value" : "AND", "children" : [
            { "value" : "X", "children" : [] },
            { "value" : "Y", "children" : [] } ]
        },
        { "value" : "XOR", "children" : [
            { "value" : "Y", "children" : [] },
            { "value" : "Z", "children" : [] } ]
        } ]
    }) == [ "X", "Y", "Z" ])
    print("... done!")

def testGenerateAllInputs():
    print("Testing generateAllInputs()...", end="")
    assert(generateAllInputs(0) == [ [] ])
    assert(sorted(generateAllInputs(1)) == [ [False], [True] ])
    assert(sorted(generateAllInputs(2)) == [ [False, False], [False, True], [True, False], [True, True] ])
    assert(sorted(generateAllInputs(3)) == [ [False, False, False], [False, False, True],
        [False, True, False], [False, True, True], [True, False, False], [True, False, True],
        [True, True, False], [True, True, True] ])
    print("... done!")

def testEvalTree():
    print("Testing evalTree()...", end="")
    # basic inputs
    assert(evalTree({ "value" : "X", "children" : []}, { "X" : False }) == False)
    assert(evalTree({ "value" : "X", "children" : []}, { "X" : True }) == True)
    not_y = { "value" : "NOT", "children" : [ { "value" : "Y", "children" : [] } ] }
    assert(evalTree(not_y, { "Y" : False }) == True)
    assert(evalTree(not_y, { "Y" : True }) == False)
    x_and_y = { "value" : "AND", "children" : [
        { "value" : "X", "children" : [] },
        { "value" : "Y", "children" : [] } ]
    }
    assert(evalTree(x_and_y, { "X" : False, "Y" : False }) == False)
    assert(evalTree(x_and_y, { "X" : False, "Y" : True }) == False)
    assert(evalTree(x_and_y, { "X" : True, "Y" : False }) == False)
    assert(evalTree(x_and_y, { "X" : True, "Y" : True }) == True)
    x_or_y = { "value" : "OR", "children" : [
        { "value" : "X", "children" : [] },
        { "value" : "Y", "children" : [] } ]
    }
    assert(evalTree(x_or_y, { "X" : False, "Y" : False }) == False)
    assert(evalTree(x_or_y, { "X" : False, "Y" : True }) == True)
    assert(evalTree(x_or_y, { "X" : True, "Y" : False }) == True)
    assert(evalTree(x_or_y, { "X" : True, "Y" : True }) == True)
    x_xor_y = { "value" : "XOR", "children": [
        { "value" : "X", "children" : [] },
        { "value" : "Y", "children" : [] } ]
    }
    assert(evalTree(x_xor_y, { "X" : False, "Y" : False }) == False)
    assert(evalTree(x_xor_y, { "X" : False, "Y" : True }) == True)
    assert(evalTree(x_xor_y, { "X" : True, "Y" : False }) == True)
    assert(evalTree(x_xor_y, { "X" : True, "Y" : True }) == False)

    # more complicated expressions
    # (X AND ((NOT Y) OR Z)) OR Y
    expr_1 = { "value" : "OR", "children" : [
        { "value" : "AND", "children" : [
            { "value" : "X", "children" : [] },
            { "value" : "OR", "children" : [
                { "value" : "NOT", "children" : [
                    { "value" : "Y", "children" : [] } ]
                },
                { "value" : "Z", "children" : [] } ]
            } ]
        },
        { "value" : "Y", "children" : [] } ]
    }
    assert(evalTree(expr_1, { "X" : False, "Y" : False, "Z" : False }) == False)
    assert(evalTree(expr_1, { "X" : False, "Y" : False, "Z" : True }) == False)
    assert(evalTree(expr_1, { "X" : False, "Y" : True, "Z" : False }) == True)
    assert(evalTree(expr_1, { "X" : False, "Y" : True, "Z" : True }) == True)
    assert(evalTree(expr_1, { "X" : True, "Y" : False, "Z" : False }) == True)
    assert(evalTree(expr_1, { "X" : True, "Y" : False, "Z" : True }) == True)
    assert(evalTree(expr_1, { "X" : True, "Y" : True, "Z" : False }) == True)
    assert(evalTree(expr_1, { "X" : True, "Y" : True, "Z" : True }) == True)
    print("... done!")

def testMakeTruthTable():
    print("Testing makeTruthTable()...")
    expr = { "value" : "OR", "children" : [
        { "value" : "AND", "children" : [
            { "value" : "X", "children" : [] },
            { "value" : "OR", "children" : [
                { "value" : "NOT", "children" : [
                    { "value" : "Y", "children" : [] } ]
                },
                { "value" : "Z", "children" : [] } ]
            } ]
        },
        { "value" : "Y", "children" : [] } ]
    }
    makeTruthTable(expr)
    print("... check the table to see if it looks right!")

def week2Tests():
    testGetLeaves()
    testGenerateAllInputs()
    testEvalTree()
    testMakeTruthTable()

week2Tests()
runProgram()

#### FULL ASSIGNMENT ####

def makeModel(data):
    return

def makeView(data, canvas):
    return

def keyPressed(data, event):
    return

def mousePressed(data, event):
    return


def runInitialCircuit(data):
    return

def drawNode(canvas, value, x, y, size, lit):
    return

def drawWire(canvas, x1, y1, x2, y2, lit):
    return

#### WEEK 3 PROVIDED CODE ####

''' getTreeDepth() finds the depth of the tree, the max length from root to leaf '''
def getTreeDepth(t):
    if len(t["children"]) == 0:
        return 0
    max = 0
    for child in t["children"]:
        tmp = getTreeDepth(child)
        if tmp > max:
            max = tmp
    return max + 1

''' getTreeWidth() finds the width of the tree, the max number of nodes on the same level '''
def getTreeWidth(t):
    if len(t["children"]) == 0:
        return 0
    elif len(t["children"]) == 1:
        return max(1, getTreeWidth(t["children"][0]))
    else:
        biggestChildSize = max(getTreeWidth(t["children"][0]),
                               getTreeWidth(t["children"][1]))
        return max(1, 2 * biggestChildSize)

''' This function draws all the inputs of the circuit. They should all go on
    the left side of the screen. '''
def drawInputs(data, canvas, size):
    ''' We'll track the locations of inputs for button-pressing later on '''
    if "inputLocations" not in data:
        data["inputLocations"] = { }
    keys = list(data["inputs"].keys())
    keys.sort()

    # make the inputs centered on the Y axis
    margin = (600 - (len(keys) * size)) / 2
    centerX = size/2
    for i in range(len(keys)):
        var = keys[i]
        if var not in data["inputLocations"]:
            data["inputLocations"][var] = { }
        inp = data["inputLocations"][var]
        centerY = size * i + size/2 + margin
        # Store the location so we can use it to click buttons later on
        inp["left"] = centerX - size/2
        inp["top"] = centerY - size/2
        inp["right"] = centerX + size/2
        inp["bottom"] = centerY + size/2
        drawNode(canvas, var, centerX, centerY, size/2, data["inputs"][var])

''' This function draws a circuit tree within the specified bounding box.
    It returns the location where the node was drawn, to make drawing wires easier. '''
def drawTree(data, canvas, t, size, left, top, right, bottom):
    if "powered" not in t:
        t["powered"] = False
    centerX = (left + right) / 2
    centerY = (top + bottom) / 2
    # Don't draw the leaves- they're all on the left side of the screen!
    if len(t["children"]) == 0:
        var = t["value"]
        d = data["inputLocations"][var]
        # Instead, return the location of the leaf, to make drawing wires easier.
        return [ (d["left"] + d["right"]) / 2 + size/4,
                 (d["top"] + d["bottom"]) / 2, data["inputs"][var] ]
    elif len(t["children"]) == 1:
        drawNode(canvas, t["value"], centerX, centerY, size/2, t["powered"])
        # Position the child at the same Y position, but to the left
        [childX, childY, childOn] = drawTree(data, canvas, t["children"][0], size,
                left - size, top, right - size, bottom)
        drawWire(canvas, childX, childY, centerX - size/4, centerY, childOn)
        return [ centerX + size/4, centerY, t["powered"] ]
    else:
        drawNode(canvas, t["value"], centerX, centerY, size/2, t["powered"])
        # Split the Y dimension in half, and give each to one child.
        # Left child
        [childX, childY, childOn] = drawTree(data, canvas, t["children"][0], size,
                left - size, top, right - size, centerY)
        drawWire(canvas, childX, childY, centerX - size/4, centerY, childOn)
        # Right child
        [childX, childY, childOn] = drawTree(data, canvas, t["children"][1], size,
                left - size, centerY, right - size, bottom)
        drawWire(canvas, childX, childY, centerX - size/4, centerY, childOn)
        return [ centerX + size/4, centerY, t["powered"] ]

''' This function draws the entire circuit. It first determines the size of each
    circuit node by measuring the width/height of the tree. Then it draws the
    inputs and outputs. Then it recursively draws the circuit tree. '''
def drawCircuit(data, canvas):
    t = data["tree"]
    if "output" not in data:
        data["output"] = False
    depth = 2 + getTreeDepth(t)
    width = max(1, len(data["inputs"]), getTreeWidth(t))
    size = 600 / max(depth, width)

    drawInputs(data, canvas, size)

    outLeft, outRight = 600 - size, 600
    outTop, outBottom = 0, 600
    outX, outY = (outLeft + outRight)/2, (outTop + outBottom)/2
    drawNode(canvas, "Out", outX, outY, size/2, data["output"])

    [childX, childY, childOn] = drawTree(data, canvas, t, size,
        outLeft - size, outTop, outRight - size, outBottom)
    drawWire(canvas, childX, childY, outLeft + size/4, outY, childOn)

#### SIMULATION STARTER CODE ###

from tkinter import *

def keyEventHandler(data, canvas, event):
    if event.keysym == "Return":
        # Clear previous data, if it exists
        if "inputLocations" in data:
            del data["inputLocations"]
    keyPressed(data, event)

    canvas.delete(ALL)
    makeView(data, canvas)
    canvas.update()

def mouseEventHandler(data, canvas, event):
    mousePressed(data, event)

    canvas.delete(ALL)
    makeView(data, canvas)
    canvas.update()

def runSimulation(w, h):
    data = { }
    makeModel(data)

    root = Tk()
    canvas = Canvas(root, width=w, height=h)
    canvas.configure(bd=0, highlightthickness=0)
    canvas.pack()
    makeView(data, canvas)

    root.bind("<Key>", lambda event : keyEventHandler(data, canvas, event))
    root.bind("<Button-1>", lambda event : mouseEventHandler(data, canvas, event))

    root.mainloop()

runSimulation(600, 650)
