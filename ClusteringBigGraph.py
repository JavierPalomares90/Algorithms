# -*- coding: utf-8 -*-
# <nbformat>2</nbformat>

# <codecell>

f = open('clustering_big.txt')
line = f.readline().split()
numNodes = int(line[0])
bitSize = int(line[1])
map  = {}
vertexNumber = 0
nodes = [0] * numNodes
for line in f:
    bits = line.split()
    n = len(bits)
    node = 0
    for i in xrange(n):
        
        node += int(bits[i])*(2**i)
    map[node] = vertexNumber
    nodes[vertexNumber-1] = node
    vertexNumber+=1
    #if not node in nodes:
        #nodes.append(node)

# <codecell>

for i in xrange(numNodes):
    node = nodes[i]
    if not node in map:
        print i,node

# <codecell>

clusters = range(vertexNumber)
numFlips=276
for i in xrange(numNodes):
    # need to iterate this function over all nodes
    node = nodes[i]
    #want to find all the nodes that differ by at most 2 bits. there are 276 ways to flip 2 bits from 2
    firstVertex = map[node]
    for i in xrange(numFlips):
        bitMask = 0x0001 << i
        nodeToCheck = node ^ bitMask
        if (nodeToCheck in map):
            vertexToMerge = map[nodeToCheck]
            clusters[vertexToMerge-1] = clusters[firstVertex-1]
            map[nodeToCheck] = firstVertex
            #print 'index ',vertexToMerge-1,'set to ',firstVertex-1
            #print 'node is',node,'node to check is',nodeToCheck,'bitmask is',bitMask

# <codecell>

n = len(clusters)
sets = [None] * n
index = 0
for i in xrange(n):
    cluster = clusters[i]
    if (not cluster in sets):
        sets[index] = cluster
        index +=1
print 'k is :',index
    

# <codecell>

numNodes = len(nodes)

# <codecell>

clusters[5]

# <codecell>

a = []

# <codecell>

a.append(1)

# <codecell>

a = []* 5

# <codecell>

a

# <codecell>

a.append(1)

# <codecell>

a

# <codecell>

1116-750-250

# <codecell>


