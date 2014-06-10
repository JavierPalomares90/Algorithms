# -*- coding: utf-8 -*-
# <nbformat>2</nbformat>

# <codecell>

import sys

infinity = sys.maxint

def floyd_warshall(n, edges):

    # Do not use NxNxN arrays!
    # All we need at each step is the result
    # of the previous turn, so NxNx2 is sufficient.
    A = [[[infinity for _ in xrange(n)] for _ in xrange(n)] for _ in xrange(2)]
    
    # Base cases
    for i in xrange(n):
        for j in xrange(n):
            if i == j:
                A[0][i][j] = 0
            else:
                if ('%i,%i' % (i, j)) in edges:
                    A[0][i][j] = edges['%i,%i' % (i, j)]
                else:
                    A[0][i][j] = infinity
    
    # Dynamic programming algorithm
    for k in xrange(1, n+1):
        for i in xrange(n):
            for j in xrange(n):
                A[k % 2][i][j] = min(A[(k-1) % 2][i][j], A[(k-1) % 2][i][k-1] + A[(k-1) % 2][k-1][j]) # a bit modified because of 0-based arrays
    
    # Check for negative cycles
    for i in xrange(n):
        if A[n % 2][i][i] < 0: return None
        
    return A[n % 2]
        
    
    
def main():
    
    for i in [1,2,3]:
        print 'Graph %i:' % i
        f = open('g%i.txt' % i)
        n, m = [int(x) for x in f.readline().split()]
        edges = {}
        for line in f:
            u, v, w = [int(x) for x in line.split()]
            edges['%i,%i' % (u, v)] = w
        APSP = floyd_warshall(n, edges)
        if APSP is None:
            print ' There is a negative-cost cycle'
        else:
            shortest = infinity
            for u in xrange(n):
                for v in xrange(n):
                    if APSP[u][v] < shortest:
                        shortest = APSP[u][v]
            print ' Shortest shortest path: %i' % shortest


main()

# <codecell>


