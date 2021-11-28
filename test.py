# Will test the main.py unit conversions
# Author: Luke Garceau

import main
from assertpy import assert_that


def test():
    # First test prepnum to only print out 2 decimals
    inputVal = 25.123
    expectedOut = '25.12'
    assert_that(main.prepNum(inputVal)).is_equal_to(expectedOut)
    print('Passed prepNum assert #1')

    # Test prepnum with None
    try:
        inVal = None
        assert_that(main.prepNum(inVal))
    except ValueError as v:
        i = 0
        expectedException = 'Num cannot be null'
        assert_that(v.args[0]).is_equal_to(expectedException)
        print('Passed prepNum assert #2')

    # Test prepNum with blank string
    inputVal = ''
    expectedOut = ''
    assert_that(main.prepNum(inputVal)).is_equal_to(expectedOut)
    print('Passed prepNum assert #3')

    # Now to assert the conversions
    CONVERSIONS = [
        {
            'input': '84.2',
            'unit': 'Fahrenheit',
            'target': 'Rankine',
            'student': '543.87',
            'output': 'correct'
        },
        {
            'input': '317.33',
            'unit': 'Kelvin',
            'target': 'Fahrenheit',
            'student': '111.554',
            'output': 'incorrect'
        },
        {
            'input': '25.6',
            'unit': 'cups',
            'target': 'liters',
            'student': '6.1',
            'output': 'correct'
        },
        {
            'input': '84.2',
            'unit': 'gallons',
            'target': 'Kelvin',
            'student': '19.4',
            'output': 'invalid'
        },
        {
            'input': '6.5',
            'unit': 'Fahrenheit',
            'target': 'Rankine',
            'student': 'dog',
            'output': 'incorrect'
        },
        {
            'input': '136.1',
            'unit': 'dog',
            'target': 'Celsius',
            'student': '45.32',
            'output': 'invalid'
        },
    ]

    # Loop through the conversions list
    count = 0
    for conversion in CONVERSIONS:
        count += 1
        try:
            inputValue = conversion['input']
            unit = conversion['unit']
            target = conversion['target']
            student = conversion['student']
            output = conversion['output']
            assert_that(main.validateStudent(inputValue, unit, target, student)).is_equal_to(output)
            print('Passed validateStudent assert #'+str(count))
        except:
            print('Failed validateStudent assert #'+str(count))
            pass
    


test()