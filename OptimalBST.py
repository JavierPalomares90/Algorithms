# -*- coding: utf-8 -*-
# <nbformat>2</nbformat>

# <codecell>

frequencies = [.05,.4,.08,.04,.1,.1,.23]
n = len(frequencies)

A = zeros((n,n))
for s in xrange(n)
    for j in xrange(n):
        i = j+1
        data = zeros(i+s)
        sumProb = 0
        for m in xrange(s):
            
            k = i+m
            sumProb += frequencies[k]
        print s,sumProb
        for n in xrange(s+1):
            r=i+n
            data[n] = sumProb
            if(i < n):
                data[n] += A[i,r-1]
            if(r+1 < n):
                data[n]+=A[r+1,s+i]
        print data
        if(i<n):
            A[i,i+s] = min(data)

# <codecell>

print A

# <codecell>

xrange(10)

# <codecell>

for i in xrange(10):
    print i+1

# <codecell>

print A[0,n]

# <codecell>

A[2,2]

# <codecell>


