import numpy as np
import pandas as pd
from . import CalculationItem as CItem
from . import UnitConverter as UConv
#from CalculationItem import Weight

class CalcRadialDensity(CItem.Weight, CItem.Volume, CItem.Density):
    radius, dens = [], []
    def __init__(self, table,atoms,num_atoms):
        MW = CItem.Weight()
        Mw = MW.avgAtomicWeight(MW.calcMoleculerWeight(MW.getAtomicWeight(atoms),num_atoms), num_atoms)
        self.radius = np.cumsum(np.diff(table.iloc[:,0]))
        r3_bins = UConv.nanoBox2centiBox(np.diff(table.iloc[:,0] ** 3))
        num_bins = np.diff(table.iloc[:,1])
        self.dens = CItem.Density.calcDensity(self, CItem.Volume.calcSphereVolume(self, r3_bins), Mw, num_bins)
        #[print(self.radius[i], self.dens[i]) for i in range(len(self.radius))]
        self.result_calc = pd.DataFrame(list(zip(self.radius,self.dens)))

    def getCalculationResult(self):
        return self.result_calc

class CalcEccentricity(CItem.Eccentricity):
    def __init__(self,table):
        #Imin = np
        self.eccentricity = CItem.Eccentricity.calcEccentricity(self, table.loc[:,['Imin']].values,table.loc[:,['Imid']].values,table.loc[:,['Imaj']].values)
        #print(table.loc[:,['time']], self.eccentricity)
        self.result_calc = pd.DataFrame(list(zip(table.loc[:,['time']].values, self.eccentricity)),dtype = 'float')

    def getCalculationResult(self):
        return self.result_calc

class CalcNumberDensity(CItem.Volume, CItem.Density):
    def __init__(self, table, box_size, division_number):
        index = []
        DENSITY_PARAMETER = 1.3
        cell_size = box_size / division_number
        cell_volume = CItem.Volume.calcCubeVolume(self, cell_size[:,0], cell_size[:,1], cell_size[:,2])
        box_volume = CItem.Volume.calcCubeVolume(self, box_size[:,0], box_size[:,1], box_size[:,2])
        total_number_density = CItem.Density.calcNumberDensity(self, box_volume, len(table))
        ### PBC
        table.loc[table.X < 0,'X'] = table.loc[table.X < 0,'X'] + box_size[:,0]
        table.loc[table.X > float(box_size[:,0]),'X'] = table.loc[table.X > float(box_size[:,0]),'X'] - box_size[:,0]
        table.loc[table.Y < 0,'Y'] = table.loc[table.Y < 0,'Y'] + box_size[:,1]
        table.loc[table.Y > float(box_size[:,1]),'Y'] = table.loc[table.Y > float(box_size[:,1]),'Y'] - box_size[:,1]
        table.loc[table.Z < 0,'Z'] = table.loc[table.Z < 0,'Z'] + box_size[:,2]
        table.loc[table.Z > float(box_size[:,2]),'Z'] = table.loc[table.Z > float(box_size[:,2]),'Z'] - box_size[:,2]
        ### Count N in each Cells
        self.sentence = "box size : " + ' '.join(map(str,box_size)) + "\ndivision number" + ' '.join(map(str,division_number)) + "\nbox volume : " + str(box_volume) + "\nbox density : "
        self.sentence = self.sentence  + str(total_number_density) + "\ncell size : " + ' '.join(map(str,cell_size)) + "\ncell volume : " + str(cell_volume)
        for x in range(division_number[0]):
            for y in range(division_number[1]):
                for z in range(division_number[2]):
                    cell_table = table.loc[(table.X >= float(cell_size[:,0] * x)) &
                                           (table.X < float(cell_size[:,0] * (x+1))) &
                                           (table.Y >= float(cell_size[:,1] * y)) &
                                           (table.Y < float(cell_size[:,1] * (y+1))) &
                                           (table.Z >= float(cell_size[:,2] * z)) &
                                           (table.Z < float(cell_size[:,2] * (z+1)))]
                    ### Calc each Cells Density
                    number_density = CItem.Density.calcNumberDensity(self, cell_volume, len(cell_table))
                    ### Compare Cell Densities and Total Density
                    if number_density > total_number_density * DENSITY_PARAMETER:
                        index.extend(cell_table.id.values)
                        self.sentence = self.sentence + "\nnumber  : " + str(len(cell_table))
                        self.sentence = self.sentence + "\ncell density  : " + str(number_density)
        self.sentence = self.sentence + "\n"
        index_int = [int(i) for i in index]
        self.Hdensity_table = table[table.id.isin(index_int)]

    def getSentence(self):
        return self.sentence

    def getHighDensityTable(self):
        return self.Hdensity_table

if __name__ == "__main__":
    atoms = ['Atom_H', 'Atom_C', 'Atom_O']
    num_atoms = [10,4,1]
    print(Mw)
