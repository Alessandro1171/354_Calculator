# This file contains re-usable helper functions that were create to facilitate the creation of the special functions

def truncate_value(value):
    # truncates value to 5 values after decimal point
    if value.is_integer():
        return int(value)
    else:
        return float("{:.5f}".format(value))


def abs(value):
    if value < 0:
        return -value

    return value


def floor(x):
    if x >= 0:
        return int(x)
    else:
        return int(x) - 1


def ln(x, rounds):
    """Calculate ln(x)

    ln(x) = 2 [ (x-1)/(x+1)  + (1/3)( (x-1)/(x+1) )^3 + (1/5) ( (x-1)/(x+1) )^5 + (1/7) ( (x-1)/(x+1) )^7 + ... ]
    source: http://math2.org/math/expansion/log.htm

    """

    result = 0
    term_constant = (x - 1) / (x + 1)

    for i in range(1, rounds, 2):
        result += ((power(term_constant, i)) * (1 / i))

    return 2 * result


def power(base, exponent):
    result = 1

    for i in range(abs(exponent)):
        result *= base

    if exponent < 0:
        result = 1.0 / result

    return result


def e_power_x(x, rounds):
    """Calculate e^x

    We use the Taylor series approximation eˣ = 1 + x + x²/2! + x³/3! + ...
    Add more terms to get a better approximation
    source: https://www.omnicalculator.com/math/e-power-x

    """
    result = 1.0
    factorial = 1.0

    for i in range(1, rounds):
        factorial *= i
        term = power(x, i) / factorial
        result += term

    return result

    """
    new added part for sqrt method exclusively
    """
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
        return float(root)
    else:
        rootDecimal = ""
        if not (pairsAfterDecimal is None):
            for pair in pairsAfterDecimal:
                mainNumber = str(mainNumber) + pair
                tempDivider = ""+str(root)+str(rootDecimal)
                tempDivider = int(tempDivider) * 2
                temp = getHighestDivider(tempDivider, int(mainNumber))
                subtractor = "" + str(tempDivider) + str(temp)
                subtractor = int(subtractor) * temp
                mainNumber = int(mainNumber) - subtractor
                rootDecimal = "" + str(rootDecimal) + str(temp)
            if mainNumber == 0 or len(rootDecimal) >= 5:
                return float((str(root) +"." + rootDecimal))

        nextPair="00"
        while mainNumber != 0 and len(rootDecimal) < 5:
            mainNumber = str(mainNumber) + nextPair
            tempDivider = "" + str(root) + rootDecimal
            tempDivider = int(tempDivider) * 2
            temp = getHighestDivider(tempDivider, int(mainNumber))
            subtractor = "" + str(tempDivider) + str(temp)
            subtractor = int(subtractor) * temp
            mainNumber = int(mainNumber) - subtractor
            rootDecimal = "" + str(rootDecimal) + str(temp)
        return float((str(root) + "." + rootDecimal))

def getHighestDivider(currenDivider, currentNumber):
    if(currentNumber<1):
        return 0
    counter=1
    subtrackingValue=1.00
    while subtrackingValue < currentNumber:
        temp = ""+str(currenDivider)+str(counter)
        temp = int(temp)
        subtrackingValue = temp *counter
        counter = counter+1
    counter = int(counter)-2
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
    decimal_digits = len(str(x).split(".")[1])
    if decimal_digits > 5:
        return True
    else:
        return False


def multi_factorial(n, decrement):
    if n <= 1:
        return 1
    else:
        return n * multi_factorial(n - decrement, decrement)
