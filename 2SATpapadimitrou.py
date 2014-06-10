# -*- coding: utf-8 -*-
# <nbformat>2</nbformat>

# <codecell>

import math
import random
import gc

def papadimitrou(clauses):

    n = len(clauses)
    
    for j in xrange(int(math.log(n, 2))):
        assignment = random_assignment(n)
        i = 2*n*n
        while i > 0:
            i -= 1
            clause_index = unsatisfied_clause(clauses, assignment)
            if clause_index is None:
                return 'satisfiable'
            else:
                var_index = abs(clauses[clause_index][random.randint(0, 1)]) - 1
                assignment[var_index] = 1 - assignment[var_index]
                
    return 'unsatisfiable'
    
    
def random_assignment(n):
    return [random.randint(0, 1) for _ in xrange(n)]


def unsatisfied_clause(clauses, assignment):
    for i in xrange(len(clauses)):
        if ((clauses[i][0] < 0 and assignment[abs(clauses[i][0])-1] == 1) or \
            (clauses[i][0] > 0 and assignment[abs(clauses[i][0])-1] == 0)) and \
            ((clauses[i][1] < 0 and assignment[abs(clauses[i][1])-1] == 1) or \
            (clauses[i][1] > 0 and assignment[abs(clauses[i][1])-1] == 0)):
            return i
    return None
    
    
def main():
    for i in xrange(1, 7):
        print 'file %i' % i
        f = open('2sat%i.txt' % i)
        n = int(f.readline())
        clauses = [[int(x) for x in line.split()] for line in f]
        
        print 'result: %s\n' % papadimitrou(clauses)
        
        gc.collect()


main()

# <codecell>

for i in xrange(1,7):
    print i

# <codecell>


