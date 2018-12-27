import numpy as np
import pandas as pd

class BOX():
    def __init__(self,table):
        self.table = table

    def PBC(self, box_size):
        self.table.loc[self.table.X < 0,'X'] = self.table.loc[self.table.X < 0,'X'] + box_size[:,0]
        self.table.loc[self.table.X > float(box_size[:,0]),'X'] = self.table.loc[self.table.X > float(box_size[:,0]),'X'] - box_size[:,0]
        self.table.loc[self.table.Y < 0,'Y'] = self.table.loc[self.table.Y < 0,'Y'] + box_size[:,1]
        self.table.loc[self.table.Y > float(box_size[:,1]),'Y'] = self.table.loc[self.table.Y > float(box_size[:,1]),'Y'] - box_size[:,1]
        self.table.loc[self.table.Z < 0,'Z'] = self.table.loc[self.table.Z < 0,'X'] + box_size[:,2]
        self.table.loc[self.table.Z > float(box_size[:,2]),'Z'] = self.table.loc[self.table.Z > float(box_size[:,2]),'Z'] - box_size[:,2]

    def divisionBox(self, cell_size, division_number):
        for x in range(division_number[0]):
            for y in range(division_number[1]):
                for z in range(division_number[2]):
                    cell_table = self.table.loc[(self.table.X >= float(cell_size[:,0] * x)) &
                                                (self.table.X < float(cell_size[:,0] * (x+1))) &
                                                (self.table.Y >= float(cell_size[:,1] * y)) &
                                                (self.table.Y < float(cell_size[:,1] * (y+1))) &
                                                (self.table.Z >= float(cell_size[:,2] * z)) &
                                                (self.table.Z < float(cell_size[:,2] * (z+1)))]
                    yield cell_table


if __name__ == "__main__":
    pass
