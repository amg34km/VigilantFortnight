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
        Imin = np
        self.eccentricity = CItem.Eccentricity.calcEccentricity(self, table.loc[:,['Imin']].values,table.loc[:,['Imid']].values,table.loc[:,['Imaj']].values)
        #print(table.loc[:,['time']], self.eccentricity)
        self.result_calc = pd.DataFrame(list(zip(table.loc[:,['time']].values, self.eccentricity)),dtype = 'float')

    def getCalculationResult(self):
        return self.result_calc

if __name__ == "__main__":
    atoms = ['Atom_H', 'Atom_C', 'Atom_O']
    num_atoms = [10,4,1]
    print(Mw)
