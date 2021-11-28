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

    
    


test()