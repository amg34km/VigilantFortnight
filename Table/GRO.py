import pandas as pd
from . import TableIO

class ReadGRO(TableIO.Table):
    def __init__(self):
        self.comment_tag = '#'
        self.plot_tag = '@'
        self.skip_line_number = 2
        self.skip_footer = 0

class ReadInfoData(ReadGRO):
    def __init__(self,infofile_name = 'GROInfo.dat', section_tab = '['):
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
                elif 'output dat' in section[1]:
                    self.new_name = getLines(lines_strip, section[0])
                elif 'output gro' in section[1]:
                    self.gro_name = getLines(lines_strip, section[0])
                elif 'colname' in section[1]:
                    self.column_names = getLines(lines_strip, section[0]).split()
                elif 'division number' in section[1]:
                    self.division_number = getLines(lines_strip, section[0]).split()

class WriteGRO():
    def format(self,table,new_name,box_size):
        with open(new_name, mode='w') as f:
            f.write('ICE\n')
            f.write('{:5d}\n'.format(len(table)))
            for row in table.values.tolist():
                row[2] = int(row[2])
                line = "{0[0]:>9s}{0[1]:>6s}{0[2]:5d}{0[3]:8.3f}{0[4]:8.3f}{0[5]:8.3f}{0[6]:8.4f}{0[7]:8.4f}{0[8]:8.4f}\n".format(row)
                f.write(line)
            box="{0[0]:10.5f}{0[1]:10.5f}{0[2]:10.5f}\n".format(box_size)
            f.write(box)

def getSectionName(lines, tab):
    sections = [[i+1,line] for i,line in enumerate(lines) if tab in line]
    return sections

def getLines(lines, num_line):
    line = lines[num_line]
    return line

if __name__ == "__main__":
    GRO = ReadInfoData()
    #GRO.skip_line_number = TableIO.countCommentLine(GRO.fname,[GRO.comment_tag,GRO.plot_tag])
    groTable = GRO.makeTable()
    print(groTable)
    #print(GRO.atom_num_lists)
