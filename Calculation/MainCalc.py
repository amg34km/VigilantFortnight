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
        cell_size = box_size / division_number
        cell_volume = CItem.Volume.calcCubeVolume(self, cell_size[:,0], cell_size[:,1], cell_size[:,2])
        box_volume = CItem.Volume.calcCubeVolume(self, box_size[:,0], box_size[:,1], box_size[:,2])
        print(box_size, division_number, cell_size)
        print(cell_volume, box_volume)
        total_number_density = CItem.Density.calcNumberDensity(self, len(table), box_volume)
        print(total_number_density)

        ### PBC
        #print(table.loc[table.Y < 0, 'Y'])
        table.loc[table.Y < 0,'Y'] = 0
        #mask["Y"] = mask["Y"] + 5
        ### Count N in each Cells
        for x in range(division_number[0]):
            for y in range(division_number[1]):
                for z in range(division_number[2]):
                    #print(x,y,z)
                    pass
        ### Calc each Cells Density

        ### Compare Cell Densities and Total Density

        ### get index



if __name__ == "__main__":
    atoms = ['Atom_H', 'Atom_C', 'Atom_O']
    num_atoms = [10,4,1]
    print(Mw)
