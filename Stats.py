# -*- coding: utf-8 -*-
# <nbformat>2</nbformat>

# <codecell>

f = open('stat.txt')
leaders = [0] * 875714
for line in f:
    i = int(line.split()[0])
    leaders[i-1] = leaders[i-1] + 1
sorted(leaders,reverse = True)

# <codecell>


