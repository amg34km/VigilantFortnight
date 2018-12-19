import pandas as pd
import numpy as np
import Table.GRO as gro
import Table.TableIO as TIO
import Calculation.MainCalc as Calc

if __name__ == "__main__":
    GRO = gro.ReadInfoData()
    WGRO = gro.WriteGRO()
    source_table = GRO.makeTable()
    N_table = source_table[source_table['particles'].str.startswith('N')]
    box_size =source_table.tail(1).astype(float).dropna(how='all', axis=1).values
    Calc = Calc.CalcNumberDensity(N_table,
                                  box_size,
                                  [int(x) for x in GRO.division_number])
    high_density_table = Calc.getHighDensityTable()
    header = Calc.getSentence()
    GRO.addSentence(header,'w')
    GRO.outputTable(high_density_table,'a')
    WGRO.format(high_density_table, GRO.gro_name, box_size.flatten().tolist())
