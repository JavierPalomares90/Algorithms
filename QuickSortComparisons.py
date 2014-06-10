# -*- coding: utf-8 -*-
# <nbformat>2</nbformat>

# <codecell>

import math
import pdb
from pylab import *
from numpy import *

def GetMedian(A,m):
    mid = int(np.floor(m/2))
    if (m % 2 == 0):
        mid = mid - 1
    first = A[0]
    last = A[m-1]
    middle = A[mid]
    #print first,middle,last
    #print "\n returning:"
    if( (first < middle and middle < last) or (last < middle and middle < first)):
        #print "middle\n"
        return mid
    elif((middle < first and first < last) or (last<first and first<middle)):
        #print "first\n"
        return 0
    else:
        #print "last\n"
        return m-1
    

def QuickSortComparisons(A,n):
    if(n == 1 or n == 0):
        return 0
    #import pdb
    #pdb.set_trace()
    #index = ChoosePivotIndex(A,0,len(A)-1)
    index = GetMedian(A,len(A))
    #swap last/mid and first element
    
    #temp = A[index]
    #A[index] = A[n-1]
    #A[n-1] = temp
    
    temp = A[index]
    A[index] = A[0]
    A[0] = temp
    
    index = 0
    i,comparisons = Partition(A,0,len(A)-1,index)
    x = QuickSortComparisons(A[:i], len(A[:i]) )
    y = QuickSortComparisons(A[(i+1):], len(A[(i+1):]) )
    return comparisons + x + y

def ChoosePivotIndex(A,left,right):
    return left
def Partition(A,l,r,index):
    #print l,r,index
    p = A[l]
    i = l + 1
    #comp = r-1+1
    comp = len(A)-1
    for j in xrange(l+1,r+1,1):
        if(A[j] < p):
            #import pdb
            #pdb.set_trace()
            #comp += 1
            temp = A[i]
            A[i] = A[j]
            A[j] = temp
            i = i + 1
    #import pdb
    #pdb.set_trace()
    temp = A[i-1]
    A[i-1] = p
    A[index] = temp
    return i-1,comp

# <codecell>

f = open('QuickSort.txt')
arraySize = 10000
array = np.zeros(arraySize)
for i in xrange(arraySize):
    array[i] = int(f.readline())
comparisons = QuickSortComparisons(array,arraySize)

# <codecell>

# comparisons when picking first element was 155432, incorrect, modified somethings and now getting
#162085

# <codecell>

# comparisons when picking last element was 157491, ->164123
# comparisons when using mid element was 145694, ->152129
print comparisons
for i in xrange(10):
    print array[i]

# <codecell>

import math
import pdb
from pylab import *
from numpy import *

def QuickSortComparisons(A,n):
    if(n == 1 or n == 0):
        return 0
    #import pdb
    #pdb.set_trace()
    index = ChoosePivotIndex(A,0,len(A)-1)
    #swap last and first element
    temp = A[index]
    A[index] = A[n-1]
    A[n-1] = temp
    
    i,comparisons = Partition(A,0,len(A)-1,index)
    x = QuickSortComparisons(A[:i], len(A[:i]) )
    y = QuickSortComparisons(A[(i+1):], len(A[(i+1):]) )
    return comparisons + x + y

def ChoosePivotIndex(A,left,right):
    return left
    #return right
def Partition(A,l,r,index):
    #print l,r,index
    p = A[index]
    i = index + 1
    comp = 0
    for j in xrange(l+1,r+1,1):
        comp += 1
        if(A[j] < p):
            #import pdb
            #pdb.set_trace()
            comp += 1
            temp = A[i]
            A[i] = A[j]
            A[j] = temp
            i = i + 1
    #import pdb
    #pdb.set_trace()
    temp = A[i]
    A[i] = p
    A[index] = temp
    
    return i,comp

# <codecell>

for i in xrange(5,7,1):
    print i

# <codecell>

print np.floor(6/2)

# <codecell>

6%2

# <codecell>


