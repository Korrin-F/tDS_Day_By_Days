# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt

x = np.array([[1,3],[1.1,4.5],
    [1.5,4],[1.7,5],[3,1],
    [3.5,1.1],[3.4,2.1]])


from scipy.cluster.hierarchy import dendrogram, linkage

plt.figure()
dendrogram(linkage(x,'single'), labels=range(0,7))