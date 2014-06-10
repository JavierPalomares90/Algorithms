# -*- coding: utf-8 -*-
# <nbformat>2</nbformat>

# <codecell>

class job:
    def __init__(self):
        self.weight = 0
        self.length = 0
        self.difference = 0
        self.ratio = 0

# <codecell>

import math
import copy
from pylab import *
from numpy import *
from operator import itemgetter
f = open('jobs.txt')
i = -1
numJobs = 0
jobs = []
sortedJobs = []
for line in f:
    if i == -1:
        numJobs = int(line)
        jobs = [job()]*numJobs
        sortedJobs = [job()] * numJobs
    else:
        l = line.split()
        j = job()
        weight = int(l[0])
        length = int(l[1])
        j.weight = weight
        j.length = length
        j.difference = weight - length
        j.ratio = 1.0*weight/length
        jobs[i] = j
    i=i+1
dtype = [('weight',int),('length',int),('difference',int),('ratio',double),('index',int)]
values = [(0,0,0,0,0)]*numJobs
j = 0
for j in xrange(numJobs):
    values[j] = (jobs[j].weight,jobs[j].length,jobs[j].difference,jobs[j].ratio,j)
sortedJobs = np.array(values,dtype = dtype)
# sort by difference. comp time is 69119377652
#sortedJobs = np.sort(sortedJobs,order=['difference','weight'])
# sort by ratio is 67311454237
sortedJobs = np.sort(sortedJobs,order ='ratio');

# <codecell>

j = 0
completionTime = 0
totalCost = long(0)
for j in xrange(numJobs):
    index = sortedJobs[numJobs-1-j][4]
    length = sortedJobs[numJobs-1-j][1]
    weight = sortedJobs[numJobs-1-j][0]
    ratio = sortedJobs[numJobs-1-j][3]
    difference = sortedJobs[numJobs-1-j][2]
    #print weight,length,difference,ratio
    #print sortedJobs[numJobs-1-j][3]
    completionTime += length
    cost = completionTime * weight;
    totalCost += cost
print totalCost

# <codecell>

for k in xrange(numJobs):
