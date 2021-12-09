"""Testing calculation class"""
import pytest
import pprint
from calc.history.calculator_result import CalculatorResult
from calc.calculations.addition import Addition

@pytest.fixture
def clear_history_fixture():
    """define a function that will run each time you pass it to a test, it is called a fixture"""
    # pylint: disable=redefined-outer-name
    CalculatorResult.clear_history()

@pytest.fixture
def setup_addition_calculation_fixture():
    """Fixture for addition"""
    # pylint: disable=redefined-outer-name
    addition = Addition(1, 2)
    CalculatorResult.add_calculation(addition)

def test_add_calculation_to_history(clear_history_fixture, setup_addition_calculation_fixture):
    """Check if clear history returns true"""
    # pylint: disable=unused-argument,redefined-outer-name,singleton-comparison
    assert CalculatorResult.count_history() == 1

def test_clear_calculation_history(clear_history_fixture, setup_addition_calculation_fixture):
    """Clears history"""
    # pylint: disable=unused-argument,redefined-outer-name,singleton-comparison
    assert CalculatorResult.count_history() == 1
    CalculatorResult.clear_history()
    assert CalculatorResult.count_history() == 0
    assert CalculatorResult.clear_history() == True
