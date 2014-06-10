# -*- coding: utf-8 -*-
# <nbformat>2</nbformat>

# <codecell>

class edge:
    def __init__(self):
        self.v1 = 0
        self.v2 = 0
        self.length = 0
class vertex:
    def __init__(self):
        # will keep track of edges going out of vertices
        self.edges = []
        self.explored = False
        self.leader = 0
        self.label = 0

# <codecell>

import math
import re
from pylab import *
from numpy import *
numVertices = 200
edges = []
vertices = []
for i in xrange(numVertices):
    v = vertex()
    vertices.append(v)
f = open('dijkstraData.txt')
re = re.compile('\s*,\s*')
for line in f:
    l = line.split()
    v1Index = int(l[0])
    vertices[v1Index-1].label = v1Index
    
    for j in xrange(1,len(l),1):
        n = re.split(l[j])
        v2Index = int(n[0])
        length = int(n[1])
        vertices[v2Index-1].label = v2Index
        e = edge()
        e.v1 = v1Index
        e.v2 = v2Index
        e.length = length
        vertices[v1Index-1].edges.append(e)
        vertices[v2Index-1].edges.append(e)
        edges.append(e)
X,A = Dijkstra(vertices,edges,vertices[0])

# <codecell>

def Dijkstra(vertices,edges,source):
    X = [source.label]
    A = [1000000]*len(vertices)
    A[source.label-1] = 0
    while len(X) != len(vertices):
        minLength = sys.maxint
        index = 0
        vIn = 0
        vOut = 0
        for i in xrange(len(edges)):
            # find the one that minimizes length
            if((edges[i].v1 in X) and (not edges[i].v2 in X)):
                v1Index = edges[i].v1
                v2Index = edges[i].v2
                l = A[v1Index - 1] + edges[i].length
                if (l < minLength):
                    index = i
                    minLength = l
                    vIn = v1Index
                    vOut = v2Index
            if((edges[i].v2 in X) and (not edges[i].v1 in X)):
                v1Index = edges[i].v1
                v2Index = edges[i].v2
                l = A[v2Index - 1] + edges[i].length
                if (l < minLength):
                    index = i
                    minLength = l
                    vIn = v2Index
                    vOut = v1Index
        # Add to x
        X.append(vOut)
        A[vOut - 1] = A[vIn-1] + edges[index].length
    return X,A

# <codecell>

for i in xrange(25):
    print A[i]

# <codecell>

vertices[3].label

# <codecell>

a = [3,2,1]

# <codecell>

not 4 in a

# <codecell>

j[4]

# <codecell>

1 != 0

# <codecell>

p2 = re.compile('\s*,\s*')

# <codecell>

k = p2.split('24,509909')

# <codecell>

k[1]

# <codecell>

sys.maxint

# <codecell>


