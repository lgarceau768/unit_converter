
# Author Luke Garceau
# Date: 11/23/2021
# Flexion Code Challenge v3.2
SIGNIFICANT_FIGS = 2

## Helper Functions
# Function to chop off extra decimals
def prepNum(num):
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
                if item['val'] == line:
                    validUnit = True
            for item in UNITS['temperature']:
                if item['val'] == line:
                    validUnit = True
            if not validUnit:
                print('Please enter a valid unit of measurement')
                askInput(prompt, number, unit)
            else: 
                return line

## Functions for conversions
def kelvin(num, unit):
    num = float(num)
    returnVal = num
    if unit == UNITS['temperature']['c']:
        returnVal = (num + 273.15)
    elif unit == UNITS['temperature']['k']:
        returnVal = num
    elif unit == UNITS['temperature']['f']:
        returnVal = ((num - 32) * (5/9) + 273.15)
    elif unit == UNITS['temperature']['r']:
        returnVal = (num * (5/9))
    else:
        raise ValueError('Unit of incorrect type')
    return prepNum(returnVal)

def fahrenheit(num, unit):
    num = float(num)
    returnVal = num
    if unit == UNITS['temperature']['c']:
        returnVal = (num * (9/5)) + 32
    elif unit == UNITS['temperature']['k']:
        returnVal = ((9/5) * num - 273.15) + 32
    elif unit == UNITS['temperature']['f']:
        returnVal = num
    elif unit == UNITS['temperature']['r']:
        returnVal = (num - 459.67)
    else:
        raise ValueError('Unit of incorrect type')
    return prepNum(returnVal)

def celsius(num, unit):
    num = float(num)
    returnVal = num
    if unit == UNITS['temperature']['c']:
        returnVal = num
    elif unit == UNITS['temperature']['k']:
        returnVal = (num - 273.15)
    elif unit == UNITS['temperature']['f']:
        returnVal = (num - 32) / (9/5)
    elif unit == UNITS['temperature']['r']:
        returnVal = (num - 491.67) * (5/9)
    else:
        raise ValueError('Unit of incorrect type')
    return prepNum(returnVal)

def rankine(num, unit):
    num = float(num)
    returnVal = num
    if unit == UNITS['temperature']['c']:
        returnVal = (num + 273.15) * (9/5)
    elif unit == UNITS['temperature']['k']:
        returnVal = (num * (9/5))
    elif unit == UNITS['temperature']['f']:
        returnVal = (num + 459.67)
    elif unit == UNITS['temperature']['r']:
        returnVal = num
    else:
        raise ValueError('Unit of incorrect type')
    return prepNum(returnVal)



## Units Variable
UNITS = {
    'temperature': {
        'c': {
            'val': 'celsius',
            'convert': celsius
        },
        'k': {
            'val': 'kelvin',
            'convert': kelvin
        },
        'f': {
            'val': 'fahrenheit',
            'convert': fahrenheit,
        },
        'r': {
            'val': 'rankine',
            'convert': rankine
        }
    },
    'volume': {
        'l': {
            'val': 'liters',
            'convert': ''
        },
        'tbsp': {
            'val': 'tablespoons',
            'convert': ''
        },
        'ci': {
            'val': 'cubic-inches',
            'convert': ''
        },
        'cf': {
            'val': 'cubic-feet',
            'convert': ''
        },
        'c': {
            'val': 'cups',
            'convert': ''
        },
        'g': {
            'val': 'gallons',
            'convert': ''
        }
    }
}

# main script
val = askInput('Please enter a numerical value')
unit = askInput('Please enter a unit')


