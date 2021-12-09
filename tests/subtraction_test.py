"""Testing Subtraction"""
from calc.calculations.subtraction import Subtraction

def test_static_calculation_subtraction():
    """testing static method for subtraction"""
    subtraction = Subtraction(10.0,6.0)
    assert subtraction.get_result() == 4.0