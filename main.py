
# Author Luke Garceau
# Date: 11/23/2021
# Flexion Code Challenge v3.2
SIGNIFICANT_FIGS = 2

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
        else:
            return line

## Functions for conversions (using kelvin as a base)
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

if __name__ == '__main__':
    # main script
    while True:
        val = askInput('Please enter a numerical value', True)
        print(celsius(val, 'fahrenheit'))


