import pandas as pd
from . import TableIO

class ReadOCC(TableIO.Table):
    def __init__(self):
        self.comment_tag = '#'
        self.plot_tag = '@'
        self.skip_line_number = 4
        self.skip_footer = 0

class ReadInfoData(ReadOCC):
    def __init__(self,infofile_name = 'SystemInfo.dat', section_tab = '['):
        super().__init__()
        with open(infofile_name) as f:
            lines_strip = [line.strip() for line in f.readlines()]
            sections = getSectionName(lines_strip, section_tab)
            for section in sections:
                if 'particles' in section[1]:
                    dat_col_name = getLines(lines_strip, section[0]).split()
                    table = TableIO.Table(infofile_name,dat_col_name, section[0]+1, ';')
                    self.atom_num_lists = table.makeTable()
                elif 'input' in section[1]:
                    self.fname = getLines(lines_strip, section[0])
                elif 'output' in section[1]:
                    self.new_name = getLines(lines_strip, section[0])
                elif 'colname' in section[1]:
                    self.column_names = getLines(lines_strip, section[0]).split()

def getSectionName(lines, tab):
    sections = [[i+1,line] for i,line in enumerate(lines) if tab in line]
    return sections

def getLines(lines, num_line):
    line = lines[num_line]
    return line

if __name__ == "__main__":
    OCC = ReadInfoData()
    OCC.skip_line_number = TableIO.countCommentLine(OCC.fname,[OCC.comment_tag,OCC.plot_tag])
    OCCTable = OCC.makeTable()
    print(OCCTable)
    print(OCC.atom_num_lists)
