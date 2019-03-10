import numpy as np
import pandas as pd
from scipy.spatial import distance
from . import CalculationItem as CItem
from . import UnitConverter as UConv
from . import BoxEdit, DataWrite
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
        self.result_calc = pd.DataFrame(list(zip(self.radius,self.dens)))

    def getCalculationResult(self):
        return self.result_calc

class CalcEccentricity(CItem.Eccentricity):
    def __init__(self,table):
        self.eccentricity = CItem.Eccentricity.calcEccentricity(self, table.loc[:,['Imin']].values,table.loc[:,['Imid']].values,table.loc[:,['Imaj']].values)
        self.result_calc = pd.DataFrame(list(zip(table.loc[:,['time']].values, self.eccentricity)),dtype = 'float')

    def getCalculationResult(self):
        return self.result_calc

class CalcNumberDensity(CItem.Volume, CItem.Density):
    def __init__(self, table, box_size, division_number):
        DENSITY_PARAMETER = 1.3
        LIMIT = 3.130152987
        index, cell_centers, dists = [], [], []
        Box=BoxEdit.BOX(table)
        cell_size = box_size / division_number
        cell_box = Box.divisionBox(cell_size, division_number)
        cell_volume = CItem.Volume.calcCubeVolume(self, cell_size[:,0], cell_size[:,1], cell_size[:,2])
        box_volume = CItem.Volume.calcCubeVolume(self, box_size[:,0], box_size[:,1], box_size[:,2])
        total_number_density = CItem.Density.calcNumberDensity(self, box_volume, len(table))
        Box.PBC(box_size)

        DS = DataWrite.DataSentence()
        DS.addListdata('box size',box_size)
        DS.addListdata('cell size',cell_size)
        DS.addListdata('division',division_number)
        DS.addNumdata('box volume',box_volume)
        DS.addNumdata('cell volume',cell_volume)
        DS.addNumdata('N particle number',len(table))
        DS.addNumdata('box density',total_number_density)
        DS.addNumdata('LIMIT',LIMIT)
        num = 0

        for i in range(np.prod(division_number)):
            cell_table, cell_center = next(cell_box)
            #print(cell_table)
            number_density = CItem.Density.calcNumberDensity(self, cell_volume, len(cell_table))
            if number_density >= LIMIT:
                index.extend(cell_table.id.values)
                cell_centers.append(cell_center)
                DS.addNumdata('particle number in cell',len(cell_table))
                DS.addNumdata('cell density',number_density)
                num += 1
            else:
                DS.addNumdata('particle number in cell',len(cell_table))
                DS.addNumdata('cell density',number_density)
        DS.addNumdata('cell number',num)

        index_int = [int(i) for i in index]

        #距離配列法
        for i in range(len(cell_centers)):
            for j in range(i+1, len(cell_centers)):
                dist = CItem.Distance.distance(self, cell_centers[i], cell_centers[j], box_size)
                dists.append(dist)
        np.savetxt('dist.dat', dists, delimiter=' ')

        self.sentence = DS.rerturnSentence()
        self.Hdensity_table = table[table.id.isin(index_int)]

    def getSentence(self):
        return self.sentence

    def getHighDensityTable(self):
        return self.Hdensity_table

if __name__ == "__main__":
    atoms = ['Atom_H', 'Atom_C', 'Atom_O']
    num_atoms = [10,4,1]
    print(Mw)
