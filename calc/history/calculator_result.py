"""Calculation history Class"""
from calc.calculations.addition import Addition
from calc.calculations.subtraction import Subtraction
from calc.calculations.multiplication import Multiplication
from calc.calculations.division import Division

class CalculatorResult:
    """Calculations class for history of calculations"""
    history = []
    # pylint: disable=too-few-public-methods

    @staticmethod
    def clear_history():
        """Clear history of calculations"""
        CalculatorResult.history.clear()
        return True

    @staticmethod
    def count_history():
        """Get count of history items"""
        return len(CalculatorResult.history)

    @staticmethod
    def get_last_calculation_object():
        """Get last calculation"""
        return CalculatorResult.history[-1]

    @staticmethod
    def get_last_calculation_result_value():
        """Get the last calculation"""
        calculation = CalculatorResult.get_last_calculation_object()
        return calculation.get_result()

    @staticmethod
    def get_first_calculation():
        """Get the first calculation"""
        return CalculatorResult.history[0]

    @staticmethod
    def get_calculation_from_history(num):
        """Get the calculation from history"""
        return CalculatorResult.history[num]

    @staticmethod
    def add_calculation_to_history(num):
        """Add calculation to history"""
        return CalculatorResult.history.append(num)
#

    def add_calculation(calculation):
        """Get a generic calculation from history"""
        return CalculatorResult.history.append(calculation)

    @staticmethod
    def add_addition_calculation_to_history(values):
        """Add addition calculation to history"""
        CalculatorResult.add_calculation(Addition.create(values))
        #Get the result of the calculation
        return True

    @staticmethod
    def add_subtraction_calculation_to_history(values):
        """Add subtraction calculation to history"""
        CalculatorResult.add_calculation(Subtraction.create(values))
        return True

    @staticmethod
    def add_multiplication_calculation_to_history(values):
        """Add multiplication calculation to history"""
        CalculatorResult.add_calculation(Multiplication.create(values))
        return True

    @staticmethod
    def add_division_calculation_to_history(values):
        """Add division calculation to history"""
        CalculatorResult.add_calculation(Division.create(values))
        return True
