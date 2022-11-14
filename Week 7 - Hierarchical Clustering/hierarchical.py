# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial import distance_matrix

# Data set
x = np.array([[1,3],[1.1,4.5],
    [1.5,4],[1.7,5],[3,1],
    [3.5,1.1],[3.4,2.1]])

# Visualisation
plt.scatter(x[:,0],x[:,1])
for i in range(x.shape[0]):
    plt.text(x[i,0]+0.05, x[i,1]+0.05, str(i))

# Distance matrix
dm = distance_matrix(x,x)
print(np.round(dm,2))



# Dendrograms
from scipy.cluster.hierarchy import dendrogram, linkage

plt.figure()
dendrogram(linkage(x,'single'), labels=range(0,7))
