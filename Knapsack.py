# -*- coding: utf-8 -*-
# <nbformat>2</nbformat>

# <codecell>

import sys

def knapsack(W, items):
    # bottom-up solution
    N = len(items)
    A = [[0 for _ in xrange(W)] for _ in xrange(N)]
    for i in xrange(N):
        v, w = items[i]
        for j in xrange(W):
            if j-w < 0: A[i][j] = A[i-1][j]
            else: A[i][j] = max(A[i-1][j], A[i-1][j-w] + v)
    return A[N-1][W-1]

def knapsack_optimized(W, items):
    # top-down solution with memoization via hashtable;
    # applicable for large problem instances
    N = len(items)
    A = {}
    def A_(i, j):
        if (str(i)+','+str(j)) in A: return A[str(i)+','+str(j)] # memoization
        if i == 0: return 0
        v, w = items[i]
        if j-w < 0:
            result = A_(i-1, j)
            A[str(i)+','+str(j)] = result # memoization
            return result
        else:
            result = max(A_(i-1, j), A_(i-1, j-w) + v)
            A[str(i)+','+str(j)] = result # memoization
            return result
    return A_(N-1, W-1)
    
def main():
    
    #if len(sys.argv) < 2: return
    sys.setrecursionlimit(20000)
    filename = 'knapsack_big.txt'
    f = open(filename)
    
    W, _ = [int(x) for x in f.readline().split()]
    items = []
    for line in f:
        v_str, w_str = line.split()
        v, w = int(v_str), int(w_str)
        items.append((v, w))
        
    #if len(sys.argv) >= 3 and sys.argv[2] == 'optimized':
    result = knapsack_optimized(W, items)
    #else:
        #result = knapsack(W, items)
        
    print 'Optimal value: %i' % result


main()

# <codecell>

del result

# <codecell>


