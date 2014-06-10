# -*- coding: utf-8 -*-
# <nbformat>2</nbformat>

# <codecell>

def closestPairs(distances,clusters):
    n = len(distances)
    spacing = infinity
    clustersToMerge = (0,0)
    for i in xrange(n):
        for j in xrange(i+1,n):
            if clusters[i] != clusters[j] and distances[i][j] < spacing:
                spacing = distances[i][j]
                clustersToMerge = [clusters[i],clusters[j]]
    return spacing,clustersToMerge

# <codecell>

def mergeClusters(distances,k):
    n = len(distances)
    clusters = range(n)
    for i in xrange(n-k):
        i,clustersToMerge = closestPairs(distances,clusters)
        for j in xrange(n):
            if clusters[j] == clustersToMerge[1]:
                clusters[j] = clustersToMerge[0]
    return clusters

# <codecell>

import sys
infinity = sys.maxint

f = open('clustering1.txt')
numNodes = int(f.readline())
k = 4
distances = [[0 for i in xrange(numNodes)]for j in xrange(numNodes)]
for line in f:
    #potential bug, needs to ignore first line
    v1,v2,d = [int(x) for x in line.split()]
    distances[v1-1][v2-1]=d
clusters = mergeClusters(distances,k)
maxSpacing,pairs = closestPairs(distances,clusters)
print maxSpacing

# <codecell>

print pairs

# <codecell>


