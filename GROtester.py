import pandas as pd
import numpy as np
import Table.GRO as gro
import Table.TableIO as TIO
import Calculation.MainCalc as Calc

if __name__ == "__main__":
    GRO = gro.ReadInfoData()
    source_table = GRO.makeTable()
    N_table = source_table[source_table['particles'].str.startswith('N')]
    box_size = GRO.readBoxSize()
    system_name, time = GRO.readSYSandTime()

    Calc = Calc.CalcNumberDensity(N_table, box_size, [int(x) for x in GRO.division_number])
    high_density_table = Calc.getHighDensityTable()

#    WGRO = gro.WriteGRO(system_name,time)
#    WGRO.format(high_density_table, GRO.gro_name, box_size.flatten().tolist())


    header = Calc.getSentence()
    GRO.addSentence(header,'w')
