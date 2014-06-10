# -*- coding: utf-8 -*-
# <nbformat>2</nbformat>

# <codecell>

def TwoSum(lst, target):
    '''
2-SUM algorithm via hash table.
O(n) time.
'''
    
    global hashTable
    
    for x in lst:
        y = target-x
        if y in hashTable and x != y:
            return True
        
    return False

# <codecell>

lines = open('2sum.txt').read().splitlines()
data = map(lambda x: int(x), lines)

hashTable = dict()
for x in data:
    hashTable[x] = True
count = 0
sorted_data = sorted(data)
for t in range(-10000, 10000+1): 
    if(TwoSum(data, t)):
        count += 1
print('Via hash table: ' + str(count))

# <codecell>

count

# <codecell>


