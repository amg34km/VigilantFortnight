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
    def calcCubeVolume(self, x, y, z):
        Volume = x * y * z
        return Volume

class Density():
    def calcDensity(self, volume, molecular_weight, num_particles):
        dens = molecular_weight * num_particles / volume
        return dens
    def calcNumberDensity(self, volume, num_particles):
        dens = num_particles / volume
        return dens


class Eccentricity():
    def calcEccentricity(self, min_inertia, mid_inertia, maj_inertia):
        avg_inertia = (min_inertia + mid_inertia + maj_inertia) / 3
        eccentricity = 1 - (min_inertia/avg_inertia)
        return eccentricity

class Distance():
    def distance(self, x0, x1, box_size):
        #PBCを考慮している
        x0 = np.array(x0)
        x1 = np.array(x1)
        delta = np.abs(x0 - x1)
        delta = np.where(delta > 0.5 * box_size, delta - box_size, delta)
        return np.sqrt((delta ** 2).sum(axis=-1))


if __name__ == "__main__":
    atoms = ['Atom_H', 'Atom_C', 'Atom_O']
    num_atoms = [10,4,1]
    MW = Weight()
    atomic_weights = MW.getAtomicWeight(atoms)
    Mw = MW.calcMoleculerWeight(atomic_weights, num_atoms)
    avg_Mw = MW.avgAtomicWeight(Mw, num_atoms)
    print(avg_Mw)
