import pandas as pd
import Table.XVG as XVG
import Table.TableIO as TIO
import Calculation.MainCalc as Calc

if __name__ == "__main__":
    XVG = XVG.ReadInfoData()
    XVG.skip_line_number = TIO.countCommentLine(XVG.fname,[XVG.comment_tag,XVG.plot_tag])
    table = XVG.makeTable()
    Calc = Calc.CalcRadialDensity(table,XVG.atom_num_lists.loc[:,['particle']].values.flatten(),XVG.atom_num_lists.loc[:,['num']].values.flatten())
    result_table = Calc.getCalculationResult()
    XVG.outputTable(result_table)
