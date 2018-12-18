import pandas as pd
import numpy as np
import Table.GRO as GRO
import Table.TableIO as TIO
import Calculation.MainCalc as Calc

if __name__ == "__main__":
    GRO = GRO.ReadInfoData()
    source_table = GRO.makeTable()
    N_table = source_table[source_table['particles'].str.startswith('N')]
    Calc = Calc.CalcNumberDensity(N_table,
                                  source_table.tail(1).astype(float).dropna(how='all', axis=1).values,
                                  [int(x) for x in GRO.division_number])
    indexes = Calc.getIndex()
    GRO.outputTable(indexes)
