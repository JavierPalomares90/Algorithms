# -*- coding: utf-8 -*-
# <nbformat>2</nbformat>

# <codecell>

class edge:
    def __init__(self):
        self.tail = 0
        self.head = 0
class vertex:
    def __init__(self):
        # will keep track of edges going out of vertices
        self.edges = []
        self.explored = False
        self.leader = 0
        self.label = 0

# <codecell>

import math
from pylab import *
from numpy import *

numEdges = 5105043
numVertices = 875714
edges = [edge()] * numEdges
vertices = [vertex()] * numVertices
reversedEdges = [edge()] * numEdges
reversedVertices = [vertex()] * numVertices
f = open('SCC.txt')
i = 0
for line in f:
    l = line.split()
    tail = int(l[0])
    head = int(l[1])
    e = edge()
    e.tail = tail
    e.head = head
    edges[i] = e;
    re = edge()
    re.tail = head
    re.head = tail
    reversedEdges[i] = re
    # tails are 1 indexed, have to correct for it
    # vertices are keeping track of the edges coming out from it
    vTail = vertex()
    rvTail = vertex()
    
    vHead = vertex()
    rvHead = vertex()
    
    oldEdges = vertices[tail-1].edges
    oldEdges.append(e)
    vTail.edges = oldEdges
    vTail.label = tail
    vHead.label = head
    vertices[tail-1] = vTail
    vertices[head-1] = vHead
    
    roldEdges = reversedVertices[head-1].edges
    roldEdges.append(re)
    rvTail.edges = roldEdges
    rvTail.label = head
    rvHead.label = tail
    reversedVertices[head-1] = rvTail
    reversedVertices[tail-1] = rvHead
    
    i = i+1

# <codecell>

def FirstDFSLoop(vertices,edges):
    global t
    t = 0
    global s
    for i in reversed(xrange(numVertices)):
        if(not vertices[i].explored):
            s = vertices[i]
            DFS(vertices,edges,i)

def DFS(vertices,edges,i):
    global s
    global t
    global finishingTimes
    vertices[i].leader = s
    vertices[i].explored = True;
    oldIndex = i
    for j in xrange(numEdges):
        # vertices are zero indexed!!!
        head = edges[j].head
        if(not vertices[head-1].explored):
            DFS(vertices,edges,head-1)
    finishingTimes[t] = oldIndex
    t= t + 1
    vertices[oldIndex].finishingTime = t
    
def SecondDFSLoop(vertices,edges):
    global t
    t = 0
    global s
    global finishingTimes
    i = 0
    for i in xrange(len(finishingTimes)):
        vertexIndex = finishingTimes[i]
        if(not vertices[vertexIndex].explored):
            s = vertices[i]
            DFS(vertices,edges,i)
def GetSCCs(vertices):
    leaders = [0] * numVertices
    i = 0
    for i in xrange(numVertices):
        leaderIndex = vertices[i].leader.label - 1
        leaders[leaderIndex] += 1
    sorted(leaders,reverse=True)
    return leaders

# <codecell>

def KosarajusAlgorithm(vertices,edges,reversedVertices,reversedEdges):
    # first pass through the loop
    FirstDFSLoop(reversedVertices,reversedEdges)
    SecondDFSLoop(vertices,edges)
    sccSizes = GetSCCs(vertices)
    i = 0
    for i in xrange(5):
        print sccSizes[i]
    

# <codecell>

finishingTimes = [0] * numVertices
t = 0
s = 0
i = 0

# <codecell>

KosarajusAlgorithm(vertices,edges,reversedVertices,reversedEdges)

# <codecell>

for i in xrange(numVertices):
    vertices[i].explored = False
    reversedVertices[i].explored = False

# <codecell>

finishingTimes[1]

# <codecell>

del vertices
del reversedEdges
del reversedVertices
del edges

# <codecell>

len(edges)

# <codecell>

edges[2].tail

# <codecell>

print i

# <codecell>

print len(edges)

# <codecell>

for i in xrange(numVertices):
    vertices[i].explored = False
    reversedVertices[i].explored = False

# <codecell>

edges[10].head

# <codecell>

a = [0 1

