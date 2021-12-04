"""Class for exporting data to external file"""

import pandas as pd
from calc.utilities.csv import PandasFileReader
from calc.history.calculator_result import CalculatorResult

class Export:
    """Exporting data class"""
    @staticmethod
    def export_result_csv_file():
        """Exporting the calculated result to csv file"""
        result = CalculatorResult.history
        df_result = pd.DataFrame(result, columns=['result'])
        with pd.ExcelWriter('../../tests/source/addition_result.csv', mode='a', if_sheet_exists='replace') as writer:
            df_result.to_csv(writer, sheet_name='Tested_output', index=False)
            writer.save()