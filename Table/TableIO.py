import pandas as pd

class Table(object):

    def __init__(self, fname, column_names, skip_line_number, comment_tag = ';'):
        self.fname = fname
        self.skip_line_number = skip_line_number
        self.comment_tag = comment_tag
        self.column_names = column_names
        self.skip_footer = 0


    def makeTable(self):
        self.table = pd.read_table(self.fname,sep = ' ',
                             skiprows = self.skip_line_number,
                             skipinitialspace = True,
                             comment = self.comment_tag,
                             skipfooter = self.skip_footer,
                             names = self.column_names)
        return self.table

    def addSentence(self,sentence,mode= 'w'):
        with open(self.new_name, mode=mode) as f:
            f.write(sentence)

    def outputTable(self,table):
       table.to_csv(self.new_name, sep='\t', index = False, header = False)


def countCommentLine(fname, comment_tags):
    skip_line_number = 0
    for tag in comment_tags:
        num_lines = sum(1 for line in open(fname) if tag in line)
        skip_line_number = skip_line_number + num_lines
    return skip_line_number


if __name__ == "__main__":
    fname = 'sampledata.txt'
    column_names=['id', 'func', 'x', 'y', 'z']
    table = Table( fname='sampledata.txt', column_names = column_names, skip_line_number=4)
    xvgTable = table.makeTable()
    print(xvgTable)
