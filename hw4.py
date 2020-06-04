'''
15-110 Homework 4
Name:       Jonathan Schwartz
Andrew ID:  jschwar4
'''

################################################################################

''' #1 - createPhonebook(nameList, numberList) '''

def createPhonebook(nameList, numberList):
    phoneBook = { }
    if (len(nameList) == 0):
        return phoneBook
    else:
        for i in range(len(nameList)):
            try:
                phoneBook[nameList[i]]
            except:
                phoneBook.update( {nameList[i] : numberList[i]})
    return phoneBook


''' #2 - createAuthorMap(bookMap) '''

def createAuthorMap(bookMap):
    authorMap = { }
    if not bool(bookMap):
        return authorMap
    else:
        for key in bookMap:
            if bookMap[key] in authorMap:
                authorMap[bookMap[key]].append(key)
            else:
                authorMap.update( {bookMap[key] :  [key] } )
    return authorMap

''' #3 - getStartingTeams(bracket) '''
def getStartingTeams(bracket):
    teams = [ ]

    if (bracket["left"] == None) and (bracket["right"] == None):
        return [ bracket["value"] ]
    else:
        if (bracket["right"] != None):
            rightTeams = getStartingTeams(bracket["right"])
            if type(rightTeams) is list:
                for i in range(len(rightTeams)):
                    teams.append(rightTeams[i])
            else:
                teams.append(rightTeams)
        if (bracket["left"] != None):
            leftTeams = getStartingTeams(bracket["left"])
            if type(leftTeams) is list:
                for i in range(len(leftTeams)):
                    teams.append(leftTeams[i])
            else:
                teams.append(leftTeams)
    return teams


''' #4 - evaluateExpression(exp) '''

def evaluateExpression(exp):
    sum = 0
    if exp['left'] == None and exp['right'] == None:
        return exp['value']

    operator = exp['value']
    if isinstance(exp['left']['value'], int):
        left_val = exp['left']['value']
    else:
        left_val = evaluateExpression(exp['left'])

    if isinstance(exp['right']['value'], int):
        right_val = exp['right']['value']
    else:
        right_val = evaluateExpression(exp['right'])

    if operator == "+":
        sum += (left_val + right_val)
    elif operator == "-":
        sum += (left_val - right_val)
    elif operator == "*":
        sum += (left_val * right_val)
    elif operator == "/":
        sum += (left_val / right_val)

    return sum


################################################################################
''' Test Functions '''

def testCreatePhonebook():
    print("Testing createPhonebook()...", end="")
    assert(createPhonebook(["Kelly", "Margaret", "Kelly"], ["0000", "1234", "9876"]) == { "Kelly" : "0000", "Margaret" : "1234" })
    assert(createPhonebook(["Rebecca", "Ellie", "Gayatri", "Rishab"], ["5", "3", "7", "1"]) == { "Rebecca" : "5", "Ellie" : "3", "Gayatri" : "7", "Rishab" : "1" })
    assert(createPhonebook(["Stella", "Stella", "Stella"], ["1234", "5678", "9"]) == { "Stella" : "1234" })
    assert(createPhonebook(["CMU"], ["412-268-2000"]) == { "CMU" : "412-268-2000" })
    assert(createPhonebook([ ], [ ]) == { })
    print("... done!")

def testCreateAuthorMap():
    print("Testing createAuthorMap()...", end="")
    assert(createAuthorMap({ "A Natural History of Dragons" : "Marie Brennan"}) == { "Marie Brennan" : ["A Natural History of Dragons"] })
    # We're using print here instead of assert because we do not mandate an order for the books, so your order might be different from ours
    # You should check your work visually if a print statement shows up here!
    result1 = createAuthorMap({ "The Hobbit" : "JRR Tolkein", "Harry Potter" : "JK Rowling", "Lord of the Rings" : "JRR Tolkein", "Casual Vacancy" : "JK Rowling", "A Game of Thrones" : "George RR Martin", "A Storm of Swords" : "George RR Martin" })
    answer1 = { "JRR Tolkein" : ["The Hobbit", "Lord of the Rings"], "JK Rowling" : ["Harry Potter", "Casual Vacancy"], "George RR Martin" : ["A Game of Thrones", "A Storm of Swords"] }
    if result1 != answer1:
        print("\nCheck that\n" + str(result1) + "\nhas the same values as\n" + str(answer1))
    result2 = createAuthorMap({ "A Wrinkle in Time" : "Madeline L'Engle", "The Golden Compass" : "Phillip Pullman", "The Subtle Knife" : "Phillip Pullman", "The Amber Spyglass" : "Phillip Pullman" })
    answer2 = { "Madeline L'Engle" : ["A Wrinkle in Time"], "Phillip Pullman" : ["The Golden Compass", "The Subtle Knife", "The Amber Spyglass"]}
    if result2 != answer2:
        print("\nCheck that\n" + str(result2) + "\nhas the same values as\n" + str(answer2))
    assert(createAuthorMap({ }) == { })
    print("... done!")

def testGetStartingTeams():
    print("Testing getStartingTeams()...", end="")
    # An order of teams is not specified, so we'll
    # sort your result before checking it
    t1 = { "value" : "United States",
           "left"  : { "value" : "United States",
                       "left"  : { "value" : "England",
                                   "left"  : None,
                                   "right" : None
                                 },
                       "right" : { "value" : "United States",
                                   "left"  : None,
                                   "right" : None
                                 }
                     },
            "right" : { "value" : "Netherlands",
                        "left"  : { "value" : "Netherlands",
                                    "left"  : None,
                                    "right" : None
                                  },
                        "right" : { "value" : "Sweden",
                                    "left"  : None,
                                    "right" : None
                                  }
                     }
         }
    #assert(sorted(getStartingTeams(t1)) == [ "England", "Netherlands", "Sweden", "United States" ])
    t2 = { "value" : "CMU",
           "left"  : { "value" : "CMU",
                       "left"  : None,
                       "right" : None
                     },
            "right" : { "value" : "MIT",
                        "left"  : None,
                        "right" : None
                     }
         }
    assert(sorted(getStartingTeams(t2)) == [ "CMU", "MIT" ])
    t3 = { "value" : "Kansas City",
           "left"  : { "value" : "Kansas City",
                       "left"  : { "value" : "Tennessee",
                                   "left"  : { "value" : "Tennessee",
                                               "left"  : None,
                                               "right" : None
                                             },
                                   "right" : { "value" : "Baltimore",
                                               "left"  : None,
                                               "right" : None
                                             }
                                 },
                       "right" : { "value" : "Kansas City",
                                   "left"  : { "value" : "Houston",
                                               "left"  : None,
                                               "right" : None
                                             },
                                   "right" : { "value" : "Kansas City",
                                               "left"  : None,
                                               "right" : None
                                             }
                                 }
                     },
            "right" : { "value" : "San Francisco",
                        "left"  : { "value" : "San Francisco",
                                    "left"  : { "value" : "Minnesota",
                                               "left"  : None,
                                               "right" : None
                                             },
                                    "right" : { "value" : "San Francisco",
                                               "left"  : None,
                                               "right" : None
                                             }
                                  },
                        "right" : { "value" : "Green Bay",
                                    "left"  : { "value" : "Seattle",
                                               "left"  : None,
                                               "right" : None
                                             },
                                    "right" : { "value" : "Green Bay",
                                               "left"  : None,
                                               "right" : None
                                             }
                                  }
                     }
         }
    assert(sorted(getStartingTeams(t3)) == [ "Baltimore", "Green Bay", "Houston", "Kansas City", "Minnesota", "San Francisco", "Seattle", "Tennessee" ])
    t4 = { "value" : "Five Guys",
           "left"  : { "value" : "Five Guys",
                       "left"  : { "value" : "Five Guys",
                                   "left"  : None,
                                   "right" : None
                                 },
                       "right" : { "value" : "Shake Shack",
                                   "left"  : { "value" : "Steak 'n Shake",
                                               "left"  : None,
                                               "right" : None
                                             },
                                   "right" : { "value" : "Shake Shack",
                                               "left"  : None,
                                               "right" : None
                                             }
                                 }
                     },
            "right" : { "value" : "Culver's",
                        "left"  : { "value" : "In-n-Out",
                                    "left"  : None,
                                    "right" : None
                                  },
                        "right" : { "value" : "Culver's",
                                    "left"  : None,
                                    "right" : None
                                  }
                     }
         }
    assert(sorted(getStartingTeams(t4)) == [ "Culver's", "Five Guys", "In-n-Out", "Shake Shack", "Steak 'n Shake" ])
    t5 = { "value" : "Stella",
           "left"  : None,
           "right" : None
         }
    assert(getStartingTeams(t5) == [ "Stella" ])
    print("... done!")

def testEvaluateExpression():
    print("Testing evaluateExpression()...", end="")
    # (4 - 2) * (8 / (1 + 1))
    t1 = { "value" : "*",
           "left"  : { "value" : "-",
                       "left"  : { "value" : 4,
                                   "left"  : None,
                                   "right" : None
                                 },
                       "right" : { "value" : 2,
                                   "left"  : None,
                                   "right" : None
                                 }
                     },
            "right" : { "value" : "/",
                        "left"  : { "value" : 8,
                                    "left"  : None,
                                    "right" : None
                                  },
                        "right" : { "value" : "+",
                                    "left"  : { "value" : 1,
                                               "left"  : None,
                                               "right" : None
                                             },
                                    "right" : { "value" : 1,
                                               "left"  : None,
                                               "right" : None
                                             }
                                  }
                     }
         }
    assert(evaluateExpression(t1) == 8)
    # ((9 - 1) * (6 / 3)) + ((0 / 7) + (3 * 2))
    t2 = { "value" : "+",
           "left"  : { "value" : "*",
                       "left"  : { "value" : "-",
                                   "left"  : { "value" : 9,
                                               "left"  : None,
                                               "right" : None
                                             },
                                   "right" : { "value" : 1,
                                               "left"  : None,
                                               "right" : None
                                             }
                                 },
                       "right" : { "value" : "/",
                                   "left"  : { "value" : 6,
                                               "left"  : None,
                                               "right" : None
                                             },
                                   "right" : { "value" : 3,
                                               "left"  : None,
                                               "right" : None
                                             }
                                 }
                     },
            "right" : { "value" : "+",
                        "left"  : { "value" : "/",
                                    "left"  : { "value" : 0,
                                               "left"  : None,
                                               "right" : None
                                             },
                                    "right" : { "value" : 7,
                                               "left"  : None,
                                               "right" : None
                                             }
                                  },
                        "right" : { "value" : "*",
                                    "left"  : { "value" : 3,
                                               "left"  : None,
                                               "right" : None
                                             },
                                    "right" : { "value" : 2,
                                               "left"  : None,
                                               "right" : None
                                             }
                                  }
                     }
         }
    assert(evaluateExpression(t2) == 22)
    # 1 + 2
    t3 = { "value" : "+",
           "left"  : { "value" : 1,
                       "left"  : None,
                       "right" : None
                     },
            "right" : { "value" : 2,
                        "left"  : None,
                        "right" : None
                     }
         }
    assert(evaluateExpression(t3) == 3)
    t4 = { "value" : 42,
           "left"  : None,
           "right" : None
         }
    assert(evaluateExpression(t4) == 42)
    print("... done!")

def testAll():
    testCreatePhonebook()
    testCreateAuthorMap()
    testGetStartingTeams()
    testEvaluateExpression()

testAll()
