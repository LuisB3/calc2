"""Testing the Calculator"""
import pytest
import pandas as pd

from calc.history.calculator_result import CalculatorResult
from calc.calculations.division import Division
from calc.calculations.addition import Addition
from calc.calculations.multiplication import Multiplication
from calc.calculations.subtraction import Subtraction
from calc.utilities.absolutepath import absolutepath

@pytest.fixture
def clear_history_fixture():
    """fixture to run tests"""
    # pylint: disable=redefined-outer-name
    CalculatorResult.clear_history()

def test_calculator_add_static(clear_history_fixture):
    """testing that our calculator has a static method for addition"""
    csv_reader = pd.read_csv(absolutepath("tests/files/addition.csv"))
    for index, row in csv_reader.iterrows():
        addition = Addition.create(row.value_a, row.value_b)
        addition_result = csv_reader["result"][index]
        assert addition.get_result() == addition_result

def test_calculator_subtract_static(clear_history_fixture):
    """Testing the subtract method of the calc"""
    csv_reader = pd.read_csv(absolutepath("tests/files/subtraction.csv"))
    for index, row in csv_reader.iterrows():
        subtraction = Subtraction.create(row.value_a, row.value_b)
        subtraction_result = csv_reader["result"][index]
        assert subtraction.get_result() == subtraction_result

def test_calculator_multiply_static(clear_history_fixture):
    """Testing the multiplication method of the calc"""
    csv_reader = pd.read_csv(absolutepath("tests/files/multiplication.csv"))
    for index, row in csv_reader.iterrows():
        multiplication = Multiplication.create(row.value_a, row.value_b)
        multiplication_result = csv_reader["result"][index]
        assert multiplication.get_result() == multiplication_result

def test_calculator_divide_static(clear_history_fixture):
    """Testing the division method of the calc"""
    csv_reader = pd.read_csv(absolutepath("tests/files/division.csv"))
    for index, row in csv_reader.iterrows():
        division = Division.create(row.value_a, row.value_b)
        division_result = csv_reader["result"][index]
        assert division.get_result() == division_result

