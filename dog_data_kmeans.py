import numpy as np
import scipy as sp
import sklearn
from sklearn import cluster, datasets
import matplotlib.pyplot as pl


csv=np.genfromtxt('dog.csv',delimiter=",")

k=2
kmeans=cluster.KMeans(n_clusters=k)
kmeans.fit(csv)
centroids=kmeans.cluster_centers_
labels=kmeans.labels_

for i in range(0,len(csv)):
    if kmeans.labels_[i] == 0:
        pl.plot(csv[i,0],csv[i,1], 'o', color="r")
    if kmeans.labels_[i] == 1:
        pl.plot(csv[i,0],csv[i,1],'o', color="b")
centroidone=pl.plot(centroids[0,0],centroids[0,1],'kx')
pl.setp(centroidone,ms=15.0)
centroidtwo=pl.plot(centroids[1,0],centroids[1,1],'kx')
pl.setp(centroidtwo,mew=2.0)

pl.show()