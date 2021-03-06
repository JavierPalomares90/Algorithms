# -*- coding: utf-8 -*-
# <nbformat>2</nbformat>

# <codecell>

class edge:
    def __init__(self):
        self.v1 = 0
        self.v2 = 0
        self.cost = 0
class vertex:
    def __init__(self):
        # will keep track of edges going out of vertices
        self.edges = []
        self.explored = False
        self.index = 0

# <codecell>

import math
from pylab import *
from numpy import *
import heapq
numEdges = 2184
numVertices = 500
edges = [edge()] * numEdges
vertices = [vertex()] * numVertices
f = open('edges.txt')
i = -1
currEdge = 0
currVertex = 0
for line in f:
    l = line.split()
    if (i==-1):
        i = 0
        continue
    else:
        v1Index = int(l[0])
        v2Index = int(l[1])
        
        cost = int(l[2])
        e = edge()
        e.v1 = v1Index
        e.v2 = v2Index
        e.cost = cost
        v1 = vertex()
        v2 = vertex()
        oldEdgesV1 = np.copy(vertices[v1Index-1].edges)
        oldEdgesV2 = np.copy(vertices[v2Index-1].edges)
        v1.edges = np.append(oldEdgesV1,e)
        v2.edges = np.append(oldEdgesV2,e)
        v1.index = v1Index
        v2.index = v2Index
        vertices[v1Index-1] = v1
        vertices[v2Index-1] = v2
        edges[currEdge] = e
        currEdge += 1

# <codecell>

s = (vertices[0],0)
# X is keeping track of the indices
X = [s[0].index]
T = []
# initialize keys
costs = [100000] * (numVertices)
costs[0] = 0
pairs = [(100000,0)] * (numVertices)
for j in xrange(numEdges):
    e = edges[j]
    if e.v1 == s[0].index:
        if (e.cost < costs[e.v2-1]):
            costs[e.v2-1] = e.cost
    elif e.v2 == s[0].index:
        if (e.cost < costs[e.v1 -1]):
            costs[e.v1-1] = e.cost
costs[0] = 0
for k in xrange(numVertices):
    pairs[k] = (costs[k],vertices[k].index)
pairs.pop(0)
heapq.heapify(pairs)
testIndex = pairs.index((100000,158))
while len(X) != numVertices:
    nextPair = heapq.heappop(pairs)
    cost = nextPair[0]
    vIndex = nextPair[1]
    v = vertices[vIndex-1]
    #print 'removed', vIndex
    #print 'nextPair: ',nextPair
    #print 'v: ',vIndex
    for n in xrange(len(v.edges)):
        e = v.edges[n]
        w = 0
        if (vIndex == e.v1):
            w = e.v2
        else:
            w = e.v1
        #print 'w: ',w
        oldCost = costs[w-1]
        pair = (oldCost,w)
        #print pair
        if not w in X:
            #print 'test: ',testIndex
            #print 'pair: ',pair
            indexToRemove = pairs.index(pair)
            #testPair = pairs[testIndex]
            # delete w from the heap
            #print vIndex,w,len(pairs)
            pair = pairs.pop(indexToRemove)#, remove, not pop
            #print 'popped', pair
            heapq.heapify(pairs)
            #might need to heapify again
            newCost = min(pair[0],e.cost)
            costs[w-1] = newCost
            e.cost = newCost
            #eWIndex = vertices[w-1].edges.index(e)
            #vertices[w-1].edges[eWindex].cost = newCost
            v.edges[n].cost = newCost
            pair = (newCost,pair[1])
            heapq.heappush(pairs,pair)
            #print 'pushed',pair
            if(len(X) == numVertices):
                break
        if len(X) == numVertices:
            break
    T.append(e)
    X.append(vIndex)
    if(len(X)==numVertices):
        break
    #print 'appended ',vIndex,'to X'
            
            
            

# <codecell>

totalCost = 0
for e in T:
    totalCost += e.cost
print totalCost

# <codecell>

s = vertices[0]
X = [s.index]
T =[]
minCost = 100000000
minIndex = 0
toAppend = 0
e = edge()
while len(X) != numVertices:
    minCost = 100000000
    toAppend = 0
    for i in xrange(len(edges)):
        e = edges[i]
        if e.cost < minCost and e.v1 in X and (not e.v2 in X):
            minCost = e.cost
            minIndex = i
            toAppend = e.v2
        if e.cost < minCost and e.v2 in X and (not e.v1 in X):
            minCost = e.cost
            minIndex = i
            toAppend = e.v1
    #edges.pop(minIndex)
    T.append(edges[minIndex])
    X.append(toAppend)

# <codecell>

for i in xrange(numVertices):
    if not i+1 in X:
        print i+1,'not in X'
        break

# <codecell>

print len(X)

# <codecell>

a = np.array([1])

# <codecell>

a.

