import random as rand
from scipy.spatial import distance

data = [[1,1,1],[1,1,2],[1,1,3],[1,1,4],[1,2,2],[1,2,3],[2,2,2]]
#data = [[rand.random() for i in range(n)] for i in range(n)]

dist_vec=distance.pdist(data)
print(dist_vec)
