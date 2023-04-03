import string
from array import array
'''from math import sqrt'''
def square_root_calculator(squaredNumber):
    if squaredNumber==0 or squaredNumber==1:
        return squaredNumber
    twoNumberParts=str(float(squaredNumber)).split('.')
    beforeDecimal=twoNumberParts[0]
    pairsAfterDecimal= []
    pairsBeforeDecimal = pairPart1(beforeDecimal)

    if len(twoNumberParts) >= 2:
        afterDecimal = twoNumberParts[1]
        pairsAfterDecimal = pariPart2(afterDecimal)
        print("I was here")
        print(afterDecimal)
        print(pairsAfterDecimal[0])
    else:
        pairsAfterDecimal = None

    root = 0
    mainNumber = ""
    for pair in pairsBeforeDecimal:
        mainNumber = str(mainNumber) + pair
        temp = getHighestDivider((root*2), int(mainNumber))
        subtractor=""+str((root * 2)) +str(temp)
        subtractor  = int(subtractor)*temp
        mainNumber = int(mainNumber) - subtractor
        root = "" + str(root) + str(temp)
        root = int(root)

    if mainNumber==0 and pairsAfterDecimal is None:
        print("here1")
        return float(root)
    else:
        rootDecimal = ""
        if not (pairsAfterDecimal is None):
            for pair in pairsAfterDecimal:
                print("in this loop")
                mainNumber = str(mainNumber) + pair
                tempDivider = ""+str(root)+str(rootDecimal)
                tempDivider = int(tempDivider) * 2
                temp = getHighestDivider(tempDivider, int(mainNumber))
                subtractor = "" + str(tempDivider) + str(temp)
                subtractor = int(subtractor) * temp
                mainNumber = int(mainNumber) - subtractor
                rootDecimal = "" + str(rootDecimal) + str(temp)
            if mainNumber == 0 or len(rootDecimal) >= 5:
                print("here2")
                return float((str(root) +"." + rootDecimal))

        nextPair="00"
        print("Main number:" + str(mainNumber) + " root: "+rootDecimal)
        while mainNumber != 0 and len(rootDecimal) < 5:
            mainNumber = str(mainNumber) + nextPair
            tempDivider = "" + str(root) + rootDecimal
            tempDivider = int(tempDivider) * 2
            print(str(tempDivider))
            temp = getHighestDivider(tempDivider, int(mainNumber))
            subtractor = "" + str(tempDivider) + str(temp)
            subtractor = int(subtractor) * temp
            mainNumber = int(mainNumber) - subtractor
            rootDecimal = "" + str(rootDecimal) + str(temp)
        print("here3")
        return float((str(root) + "." + rootDecimal))

def getHighestDivider(currenDivider, currentNumber):
    counter=1
    subtrackingValue=1.00
    while subtrackingValue < currentNumber:
        print(str(counter))
        temp = ""+str(currenDivider)+str(counter)
        temp = int(temp)
        '''print(temp)'''
        subtrackingValue = temp *counter
        counter = counter+1
    counter = int(counter)-2
    print(counter)
    return counter

def pairPart1(beforeDecimal):
    arrayOfPairs=[]
    if len(beforeDecimal)%2!=0:
        firstCharacter="0"+beforeDecimal[: 1]
        beforeDecimal = beforeDecimal[1: ]
        arrayOfPairs.append(firstCharacter)
    else:
        firstTwoCharacter =  beforeDecimal[: 2]
        beforeDecimal = beforeDecimal[2:]
        arrayOfPairs.append(firstTwoCharacter)
    while beforeDecimal!="":
        characterPair = beforeDecimal[: 2]
        beforeDecimal = beforeDecimal[2:]
        arrayOfPairs.append(characterPair)
    return arrayOfPairs
def pariPart2(afterDecimal):
    arrayOfPairs = []

    while len(afterDecimal) > 1:
        characterPair = afterDecimal[: 2]
        afterDecimal = afterDecimal[2:]
        arrayOfPairs.append(characterPair)
    if len(afterDecimal) == 1:
        arrayOfPairs.append((afterDecimal+"0"))
    return arrayOfPairs
def check_decimal(x):
    decimal_digits = len(str(x).split('.')[1])
    if decimal_digits > 5:
        return True
    else:
        return False
def standard_deviation(input=string, population=bool):
    data = input.split(",")
    n = 0.0
    ln(n)
    if population:
        n = len(data)
    else:
        n = len(data)-1
    mean = 0.0
    for x in data:
        mean += float(x)
    sum = 0.0
    mean = float(mean) / len(data)
    for x in data:
        sum += (float(x) - mean)
    standard_deviation_value = sum * sum
    standard_deviation_value = standard_deviation_value/n
    standard_deviation_value = square_root_calculator(standard_deviation_value)
    if check_decimal(standard_deviation_value):
        standard_deviation_value = round(standard_deviation_value, 5)
    return standard_deviation_value
x = square_root_calculator(2376.592)
print(x)