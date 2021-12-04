"""This is the multiplication calculation that inherits the values from the calculations class"""
#This is called a namespace it is like files & folders.
#It looks like a folder & file path but it is a like a virtual representation

from calc.calculations.calculation import Calculation

#This is how you extend the Addition class with the Calculation
class Multiplication(Calculation):
    """The addition class has one method to get the result of the calculation"""
    def get_result(self):
        """getting the multiplication results"""
        #return self.value_a * self.value_b
        for index, value in enumerate(self.values):
            if index == 0:
                multiplication_value = value
            else:
                multiplication_value = multiplication_value * value
        return multiplication_value