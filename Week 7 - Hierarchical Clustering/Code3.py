# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D #in order to do 3d plots
from sklearn import datasets

# Load the iris dataset
irisdata = datasets.load_iris()

# Get the iris data
x = irisdata.data
x_labs = irisdata.target
labels = np.unique(x_labs) #get unique labels

# Visualize in 3D
d = [0,1,3] #which dimensions to use

fig = plt.figure()
ax = plt.axes(projection ="3d")
ax.set_title('Iris dataset')

for i, j in enumerate(x_labs):
    if j==labels[0]:
        ax.scatter3D(x[i,d[0]],x[i,d[1]],x[i,d[2]], marker='o', color='red')
    elif j==labels[1]:
        ax.scatter3D(x[i,d[0]],x[i,d[1]],x[i,d[2]], marker='o', color='green')
    else:
        ax.scatter3D(x[i,d[0]],x[i,d[1]],x[i,d[2]], marker='o', color='blue')   


#-----------------------------------------------------------------------


# Generate the dendrogram (4 linkage methods)
from scipy.cluster.hierarchy import dendrogram, linkage

fig, axes = plt.subplots(2,2)
fig.tight_layout(pad=3.0)

dendrogram(linkage(x,'single'), ax=axes[0,0])
axes[0,0].set_title('Single linkage')

dendrogram(linkage(x,'complete'), ax=axes[0,1])
axes[0,1].set_title('Complete linkage')

dendrogram(linkage(x,'average'), ax=axes[1,0])
axes[1,0].set_title('Average linkage')

dendrogram(linkage(x,'ward'), ax=axes[1,1])
axes[1,1].set_title('Ward linkage')


#-----------------------------------------------------------------------


# Agglomerative clustering (4 linkage methods)
from sklearn.cluster import AgglomerativeClustering

k = 3
metric = 'euclidean'
linkage_criteria = ['single','complete','average','ward']
clustering_result = []

for i in linkage_criteria:
    myCluster = AgglomerativeClustering(n_clusters=k, affinity='euclidean', linkage=i)
    clustering_result.append(myCluster.fit_predict(x))
    
    
# Visualize
fig = plt.figure()
fig.tight_layout(pad=3.0)
i_plt = 1    #subplot index
d = [0,1,2]  #which dimensions to use

for links in clustering_result:
    ax = fig.add_subplot(2, 2, i_plt, projection='3d')
    ax.set_title(linkage_criteria[i_plt-1])
    
    for i, j in enumerate(links):
        if j==labels[0]:
            ax.scatter3D(x[i,d[0]],x[i,d[1]],x[i,d[2]], marker='o', color='red')
        elif j==labels[1]:
            ax.scatter3D(x[i,d[0]],x[i,d[1]],x[i,d[2]], marker='o', color='green')
        else:
            ax.scatter3D(x[i,d[0]],x[i,d[1]],x[i,d[2]], marker='o', color='blue')   
        
    i_plt +=1
    
    
    
