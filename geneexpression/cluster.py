#! /usr/bin/env python

import sys
from matplotlib import pyplot as plt
from scipy.cluster.hierarchy import dendrogram, linkage
import numpy as np
import scipy


data = sys.stdin

colHeaders = data.next().strip().split()[1:]
rowHeaders = []
dataMatrix = []

#print colHeaders

for line in data:
	fields = line.strip().split('\t')
	rowHeaders.append(fields[0])
	dataMatrix.append([float(x) for x in fields[1:]])

dataMatrix = np.array(dataMatrix) 

z1 = linkage(dataMatrix)
z2 = linkage(dataMatrix.T)

#indexes = leaves_list(z1)

#cell type clustering
plt.figure(figsize=(25, 10))
plt.title('Cell Type Hierarchical Clustering')
plt.xlabel('sample index')
plt.ylabel('distance')
dendrogram(
    z2,
    #leaf_rotation=90.,  # rotates the x axis labels
    leaf_font_size=12.,  # font size for the x axis labels
)
#plt.show()
plt.savefig("celltype_cluster.png")

#gene clusterin
plt.figure(figsize=(25, 10))
plt.title('Gene Hierarchical Clustering')
plt.xlabel('sample index')
plt.ylabel('distance')
dendrogram(
    z1,
    #leaf_rotation=90.,  # rotates the x axis labels
    )
#plt.show()
plt.savefig("gene_cluster.png")

#heatmap
plt.figure()
plt.imshow(dataMatrix, cmap='hot', interpolation='nearest')
#plt.show()
plt.savefig("heatmap.png")


