# -*- coding: utf-8 -*-
# <nbformat>2</nbformat>

# <codecell>

import math
from pylab import *
from numpy import *
f = open('IntegerArray.txt')
arraySize = 100000
array = np.zeros(arraySize)
for i in xrange(arraySize):
    array[i] = int(f.readline())
A,inversions = SortAndCount(array,arraySize)
print inversions

# <codecell>

def SortAndCount(array,size):
    if size == 1:
        return array,0;
    else:
        b,x = SortAndCount(array[:int(size/2)],int(size/2))
        c,y = SortAndCount(array[int(size/2):],size - int(size/2))
        d,z = CountSplitInv(array,size)
        return d,x+y+z
def CountSplitInv(array,size):
    inversions = 0
    halfLen = int(size/2)
    b = sorted(array[:halfLen])
    c = sorted(array[halfLen:])
    d = np.zeros(size);
    i = 0
    j = 0
    k = 0
    halfLen = len(b)
    latterLen = len(c)
    while (i < halfLen or j < latterLen):
        if(i == halfLen):
            d[k] = c[j]
            j+=1
        elif(j == latterLen):
            d[k] = b[i]
            i+=1
    #while(k < size and i < halfLen and j < latterLen):
        elif(b[i] < c[j]):
            d[k] = b[i]
            i+=1
        else:
            d[k] = c[j]
            j+=1
            inversions += halfLen-i
        k += 1
    return d, inversions

# <codecell>

from IPython.core.debugger import Pdb

# <codecell>

def count_inversions(source):
    if len(source) <= 1:
        return 0, source
    
    mid = len(source) // 2
    left = source[:mid]
    right = source[mid:]
    
    countLeft, left = count_inversions(left)
    countRight, right = count_inversions(right)
    
    countMerged, merged = merge_and_count(left, right)
    
    return countLeft + countRight + countMerged, merged

def merge_and_count(left, right):
    merged = []
    i, j = 0, 0
    count = 0
    
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
            count += len(left) - i
    
    while i < len(left):
        merged.append(left[i])
        i += 1
        
    while j < len(right):
        merged.append(right[j])
        j += 1
               
    return count, merged

