# -*- coding: utf-8 -*-
# <nbformat>2</nbformat>

# <codecell>

from pylab import *
from numpy import *
import math
import heapq
heapLow = []
heapHigh = []

lines = open('Median.txt').read().splitlines()
data = map(lambda x: int(x), lines)
medians = []

for x in data:
    # insert into the heaps
    median = InsertElem(x)
    medians.append(median)
print(reduce(lambda x,y: (x+y) % 10000, medians))

# <codecell>

def InsertElem(x):
    global heapLow
    global heapHigh
    # make heapLow a min heap by negating elements
    if(len(heapLow) == 0):
        heapq.heappush(heapLow,-x)
    else:
        prevMed = -heapLow[0];
        # add x to the heap it belongs to
        if(x > prevMed):
            heapq.heappush(heapHigh,x)
            #Balance the heaps
            if len(heapHigh) > len(heapLow):
                y = heapq.heappop(heapHigh)
                heapq.heappush(heapLow, -y)
            
        else:
            heapq.heappush(heapLow,-x)
            if len(heapLow) - len(heapHigh) >1:
                y = -heapq.heappop(heapLow)
                heapq.heappush(heapHigh,y)
    return -heapLow[0]
    

# <codecell>

len(data)

# <codecell>


