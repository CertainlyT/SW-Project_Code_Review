from math import factorial as fact

def factorial(numStr):
    numStr = incorrectFloat(numStr)
    try:
        n = int(numStr)
        r = str(fact(n))
    except:
        r = 'Error!'
    return r

def decToBin(numStr):
    numStr = incorrectFloat(numStr)
    try:
        n = int(numStr)
        r = bin(n)[2:]
    except:
        r = 'Error!'
    return r

def binToDec(numStr):
    numStr = incorrectFloat(numStr)
    try:
        n = int(numStr, 2)
        r = str(n)
    except:
        r = 'Error!'
    return r

def decToRoman(numStr):
    return 'dec -> Roman'

def incorrectFloat(numStr):
    # incorrect result when clac 0.1 * 0.2 etc...
    numStr = str(eval(numStr))
    if any('.' in onenum for onenum in numStr):
        zero = 0
        for i in range(numStr.index('.') + 1, len(numStr)):
            if zero == 5:
                numStr = (str(numStr)[0:i - 5])
            else:
                if str(numStr)[i] == '0':
                    zero += 1
                else:
                    zero = 0
    return numStr

