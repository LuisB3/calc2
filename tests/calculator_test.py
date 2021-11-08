"""Testing the Calculator"""
from calculator.main import Calculator

def test_calculator_result():
    """testing calculator result is 0"""
    calc = Calculator()
    assert calc.result == 0

def test_calculator_add():
    """Testing the Add function of the calculator"""
    #Arrange by instantiating the calc class
    calc = Calculator()
    #Act by calling the method to be tested
    calc.add_number(5)
    #Assert that the results are correct
    assert calc.result == 5

def test_calculator_get_result():
    """Testing the Get result method of the calculator"""
    calc = Calculator()
    assert calc.get_result() == 0

def test_calculator_subtract():
    """Testing the subtract method of the calculator"""
    calc = Calculator()
    calc.subtract_number(3)
    assert calc.get_result() == -3

def test_calculator_multiply():
    """ tests multiplication of two numbers"""
    calc = Calculator()
    result  = calc.multiply_numbers(5,9)
    assert result == 45

def test_calculator_divide():
    """ tests division of two numbers"""
    calc = Calculator()
    result  = calc.divide_numbers(10,5)
    assert result == 2

def test_calculator_cube():
    """ tests cube of a number"""
    calc = Calculator()
    result  = calc.cube_numbers(3)
    assert result == 27
