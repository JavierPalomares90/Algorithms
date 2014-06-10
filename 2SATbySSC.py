# -*- coding: utf-8 -*-
# <nbformat>2</nbformat>

# <codecell>

import math
import random
import gc
import sys
import threading
from StringIO import StringIO

def make_sat_graph(clauses):
    n = len(clauses)
    def var_index(var):
        if var < 0: return n - var
        else: return var
    res = ''
    for clause in clauses:
        res += '%i %i\n' % (var_index(-clause[0]), var_index(clause[1]))
        res += '%i %i\n' % (var_index(-clause[1]), var_index(clause[0]))
    return res
        
        
################################################################################
####### Kosaraju's SSC algorithm implementation from part 1 ######
################################################################################

def readDirectedGraph(str):
    f = StringIO(str)
    
    adjlist = []
    adjlist_reversed = []
    
    line = f.readline()
    while line != '':
        num1, num2 = line.split()
        v_from = int(num1)
        v_to = int(num2)
        max_v = max(v_from, v_to)
        
        while len(adjlist) < max_v:
            adjlist.append([])
        while len(adjlist_reversed) < max_v:
            adjlist_reversed.append([])
            
        adjlist[v_from-1].append(v_to-1)
        adjlist_reversed[v_to-1].append(v_from-1)
        
        line = f.readline()
            
    return adjlist, adjlist_reversed


t = 0
s = None
n = 0
explored = None
leader = None
current_ssc = None
contradictory_ssc = None
sorted_by_finish_time = None

def DFS_Loop_1(graph_rev, n):
    
    global t, explored, sorted_by_finish_time
    
    t = 0
    explored = [False]*n
    sorted_by_finish_time = [None]*n
    
    for i in reversed(range(n)):
        if not explored[i]:
            DFS_1(graph_rev, i)
                        
            
def DFS_1(graph_rev, i):
    
    global t, explored
    
    explored[i] = True
    
    for v in graph_rev[i]:
        if not explored[v]:
            DFS_1(graph_rev, v)
    
    sorted_by_finish_time[t] = i
    t += 1
    
    
def DFS_Loop_2(graph):
    
    global current_ssc, explored, contradictory_ssc, sorted_by_finish_time
    
    explored = [False]*len(graph)
    
    for i in reversed(range(len(graph))):
        if not explored[sorted_by_finish_time[i]]:
            scc_size = 0
            # Here we collect all the members
            # of the next SCC using DFS.
            current_ssc = set()
            contradictory_ssc = False
            DFS_2(graph, sorted_by_finish_time[i])
            if contradictory_ssc: break
            
    return contradictory_ssc
    
    
def DFS_2(graph, i):
    
    global explored, current_ssc, contradictory_ssc
    
    explored[i] = True
    current_ssc.add(i)
    
    # Check for unsatisfabilty indicator
    if i < n:
        if (i+n) in current_ssc:
            contradictory_ssc = True
    elif (i-n) in current_ssc:
        contradictory_ssc = True
    
    for v in graph[i]:
        if not explored[v]:
            DFS_2(graph, v)
    

def kosaraju_contradictory_ssc(graph, graph_rev):
    
    DFS_Loop_1(graph_rev, len(graph))
    contradictory_ssc = DFS_Loop_2(graph)
    
    return contradictory_ssc


def main():

    global n

    for i in xrange(1, 7):
        print 'file %i' % i
        f = open('2sat%i.txt' % i)
        n = int(f.readline())
        clauses = [[int(x) for x in line.split()] for line in f]
        
        sat_graph = make_sat_graph(clauses)
        graph, graph_rev = readDirectedGraph(sat_graph)
        contradictory_ssc = kosaraju_contradictory_ssc(graph, graph_rev)
        res = 'unsatisfiable' if contradictory_ssc else 'satisfiable'
        
        print 'result: %s\n' % res
        
        gc.collect()


if __name__ == '__main__':
    threading.stack_size(67108864) # 64MB stack
    sys.setrecursionlimit(2 ** 20) # approx 1 million recursions
    thread = threading.Thread(target = main) # instantiate thread object
    thread.start() # run program at target

# <codecell>

main()

# <codecell>


