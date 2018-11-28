import numpy as np
import pandas as pd
from operator import mul
from . import ChemistItem

AVOGADRO=6.022e+23

class Weight():
    def getAtomicWeight(self,atoms):
        return ChemistItem.atomicWeight(atoms)

    def calcMoleculerWeight(self,atomic_weights,num_atoms):
        Mw = sum(map(mul, atomic_weights, num_atoms)) / (AVOGADRO)
        return Mw

    def avgAtomicWeight(self,Mw, num_atoms):
        return Mw / sum(num_atoms)

class Volume():
    def calcSphereVolume(self, radius):
        Volume = 4 * np.pi * radius / 3
        return Volume

class Density():
    def calcDensity(self, volume, molecular_weight, num_atom):
        dens = molecular_weight * num_atom / volume
        return dens

class Eccentricity():
    def calcEccentricity(self, min_inertia, mid_inertia, maj_inertia):
        avg_inertia = (min_inertia + mid_inertia + maj_inertia) / 3
        eccentricity = 1 - (min_inertia/avg_inertia)
        return eccentricity


if __name__ == "__main__":
    atoms = ['Atom_H', 'Atom_C', 'Atom_O']
    num_atoms = [10,4,1]
    MW = Weight()
    atomic_weights = MW.getAtomicWeight(atoms)
    Mw = MW.calcMoleculerWeight(atomic_weights, num_atoms)
    avg_Mw = MW.avgAtomicWeight(Mw, num_atoms)
    print(avg_Mw)
