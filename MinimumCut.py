# -*- coding: utf-8 -*-
# <nbformat>2</nbformat>

# <codecell>

import math
from pylab import *
from numpy import *
import random
import copy
numVertices = 8
vertices = [vertex()]*numVertices
edges = []*1000
f = open('test.txt')
for line in f:
    i = line.split()
    v1Index = int(i[0])
    v1 = vertex()
    for j in xrange(1,len(i)):
        v2Index = int(i[j])
        edg = edge()
        edg.v1 = v1Index
        edg.v2 = v2Index
        # each vertex is keeping track of its edges
        v1.edges[j-1] = edg
        # only add edges that are not in the list
        edges.append(edg)
    v1.edges = v1.edges[0:j]
    vertices[v1Index-1] = v1
minCut = len(edges)
numIterations = 10
for i in xrange(0,numIterations):
    backupEdges = copy.deepcopy(edges)
    backupVertices = copy.deepcopy(vertices)
    cut = KargerMinCut(backupVertices,backupEdges)
    if(cut < minCut):
        minCut = cut
# doubles the min cut when there are parallel edges
print 'smallest cut was: ',minCut

# <codecell>

class edge:
    def _init_(self):
        # will keep track of the two vertices only by their number
        self.v1 = 0;
        self.v2 = 0;

class vertex:
    def __init__(self):
        self.edges = [edge()]* (numVertices -1) 

# <codecell>

def KargerMinCut(vertices,edges):
    numLoops = len(vertices)-2
    for i in xrange(0,numLoops):
        index = random.randint(0,len(edges)-1)
        edges = ContractEdge(vertices,edges,index)
    if(len(edges) == 2):
        for i in xrange(0,len(edges)):
            print edges[i].v1,edges[i].v2
    return len(edges)
        
        
def ContractEdge(vertices,edges,index):
    edge = edges[index]
    # Remove the edge from the list
    edges.pop(index)
    # the two vertices at ends of the edge
    v1 = edge.v1;
    v2 = edge.v2;
    # combine the edges of v1 and v2
    #v1Edges = vertices[v1-1].edges
    #v2Edges = vertices[v2-1].edges
    #vEdges = v1Edges + v2Edges
    #flag = False
    #i = 0
    # remove self loops (any additional loops from v1 to v2)
    #while (not flag):
     #   if(i == (len(vEdges) - 1)):
      #      flag = True
       # if(vEdges[i].v2 == v2 or vEdges[i].v2 == v1):
        #    vEdges.pop(i)
        #else:
         #   i+=1
    # contract v1 and v1
    i = 0
    flag = True
    while(flag):
        if(i>len(edges)-1 or i <0):
            print 'fault',i
        if(edges[i].v1 == v2):
            edges[i].v1 = v1
        if(edges[i].v2 == v2):
            edges[i].v2 = v1
        # remove self loops
        if(edges[i].v1 == edges[i].v2):
            edges.pop(i)
            i -=1
        if(i == (len(edges)-1)):
            flag = False
        else:
            i += 1
    #vertices[v1-1].edges = vEdges;
    return edges

# <codecell>

len(vertices)

# <codecell>

e = edge();
e.v1 = 1;
e.v2 = 2

# <codecell>

edges[0].v2

# <codecell>

print len(vertices)

# <codecell>

len(vertices)

# <codecell>

len(edges)

# <codecell>

