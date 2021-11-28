
# Author Luke Garceau
# Date: 11/23/2021
# Flexion Code Challenge v3.2
SIGNIFICANT_FIGS = 2
ROUNDING_ERROR = 0.05

## Units Variable
UNITS = {
    'temperature': {
        'c': {
            'val': 'celsius',
        },
        'k': {
            'val': 'kelvin',
        },
        'f': {
            'val': 'fahrenheit',
        },
        'r': {
            'val': 'rankine',
        }
    },
    'volume': {
        'l': {
            'val': 'liters',
        },
        'tbsp': {
            'val': 'tablespoons',
        },
        'ci': {
            'val': 'cubic-inches',
        },
        'cf': {
            'val': 'cubic-feet',
        },
        'c': {
            'val': 'cups',
        },
        'g': {
            'val': 'gallons',
        }
    }
}

## Helper Functions
# Function to chop off extra decimals
def prepNum(num):
    if num == None:
        raise ValueError('Num cannot be null')
    if num == '':
        return num
    line = str(num)
    if line.find('.') == -1:
        return line
    else:
        return line[:line.find('.')+SIGNIFICANT_FIGS+1]
        
# Function to validate the number inputted
def isValidNumber(str):
    try:
        float(str)
        return True
    except ValueError:
        return False

# Function to prompt the user for input and validate the input
def askInput(prompt, number=False, unit=False):
    line = input(prompt+': ')
    if line == '':
        askInput(prompt, number, unit)
    else:
        if number:
            if isValidNumber(line):
                return line
            else:
                print('Please enter a valid number')
                askInput(prompt, number, unit)
        elif unit:
            line = line.lower().rstrip()
            validUnit = False
            for item in UNITS['volume']:
                if UNITS['volume'][item]['val'] == line:
                    validUnit = True
            for item in UNITS['temperature']:
                if UNITS['temperature'][item]['val'] == line:
                    validUnit = True
            if not validUnit:
                print('Please enter a valid unit of measurement')
                askInput(prompt, number, unit)
            else: 
                return line
        else:
            return line

# Funciton to pull unit key from input
def getUnit(inputVal):
    refUnit = ''
    temp = False
    for unit in UNITS['temperature']:
        if UNITS['temperature'][unit]['val'] == inputVal:
            refUnit = unit
            temp = True
    for unit in UNITS['volume']:
        if UNITS['volume'][unit]['val'] == inputVal:
            refUnit = unit
    if refUnit == '':
        raise ValueError('Invalid unit input')
    else:
        if temp:
            unitFamily = 'temperature'
        else:
            unitFamily = 'volume'
        return [refUnit, unitFamily]

# Function to validate student input
def validateStudent(num, startUnit, targetUnit, studentInput):
    # need to pull out the conversion function from the units table    
    try:       
        [tUnit, unitFamily] = getUnit(targetUnit.lower())
        answerVal = UNITS[unitFamily][tUnit]['convert'](num, startUnit.lower()) 
        try:
            isWithinRoundingError = float(studentInput) >= (float(answerVal) - ROUNDING_ERROR) and float(studentInput) <= (float(answerVal) + ROUNDING_ERROR)
        except:
            return 'incorrect'
        if isWithinRoundingError:
            return 'correct'
        else:
            return 'incorrect'  
    except:
        return 'invalid'

## Functions for conversions (using kelvin and liters as a base)
def kelvin(num, unit):
    num = float(num)
    returnVal = num
    if unit == UNITS['temperature']['c']['val']:
        returnVal = (num + 273.15)
    elif unit == UNITS['temperature']['k']['val']:
        returnVal = num
    elif unit == UNITS['temperature']['f']['val']:
        returnVal = ((num - 32) * (5/9) + 273.15)
    elif unit == UNITS['temperature']['r']:
        returnVal = (num * (5/9))
    else:
        raise ValueError('Unit of incorrect type')
    return prepNum(returnVal)

def fahrenheit(num, unit):
    return prepNum(((9/5) * float(kelvin(num, unit)) - 273.15) + 32)

def celsius(num, unit):
    return prepNum(float(kelvin(num, unit)) - 273.15)

def rankine(num, unit):
    return prepNum(float(kelvin(num, unit)) * (9/5))

def liters(num, unit):
    num = float(num)
    returnVal = num
    if unit == UNITS['volume']['l']['val']:
        returnVal = num
    elif unit == UNITS['volume']['tbsp']['val']:
        returnVal = (num / 67.63)
    elif unit == UNITS['volume']['ci']['val']:
        returnVal = (num * 0.016387)
    elif unit == UNITS['volume']['cf']['val']:
        returnVal = (num / 0.035315)
    elif unit == UNITS['volume']['c']['val']:
        returnVal = (num / 4.2268)
    elif unit == UNITS['volume']['g']['val']:
        returnVal = (num * 3.785)
    else:
        raise ValueError
    return prepNum(returnVal)

def tablespoons(num, unit):
    return (float(liters(num, unit)) * 67.63)

def cubicInches(num, unit):
    return (float(liters(num, unit)) * 61.02)

def cubicFeet(num, unit):
    return (float(liters(num, unit)) * 0.035315)

def cups(num, unit):
    return (float(liters(num, unit)) * 4.2268)

def gallons(num, unit):
    return (float(liters(num, unit)) * 0.2641)

# Attach all the conversion functions to the units variable
for item in UNITS['temperature']:
    if item == 'c':
        UNITS['temperature'][item]['convert'] = celsius
    if item == 'f':
        UNITS['temperature'][item]['convert'] = fahrenheit
    if item == 'r':
        UNITS['temperature'][item]['convert'] = rankine
    if item == 'k':
        UNITS['temperature'][item]['convert'] = kelvin
for item in UNITS['volume']:
    if item == 'c':
        UNITS['volume'][item]['convert'] = cups
    if item == 'ci':
        UNITS['volume'][item]['convert'] = cubicInches
    if item == 'cf':
        UNITS['volume'][item]['convert'] = cubicFeet
    if item == 'g':
        UNITS['volume'][item]['convert'] = gallons
    if item == 'l':
        UNITS['volume'][item]['convert'] = liters
    if item == 'tbsp':
        UNITS['volume'][item]['convert'] = tablespoons


# main script
if __name__ == '__main__':
    while True:
        print(validateStudent(
            askInput('Please enter a numerical value', True),
            askInput('Please enter a unit of measure', False, True),
            askInput('Please enter the target unit of measure', False, True),
            askInput('Please enter the student answer', True)
        ))

