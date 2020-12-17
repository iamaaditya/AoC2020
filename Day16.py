import re

data = open('input.txt').read().splitlines()
rules = data[0:20]
near = [list(map(int, i.split(','))) for i in data[25:]]
my = [int(i) for i in data[22].split(',')]

p = re.compile('(\d*)-(\d*) or (\d*)-(\d*)')
rg = {}
for r in rules:
    rg[r.split(':')[0]] = list(map(int, re.findall(p, r)[0]))

def check(a):
    for k, r in rg.items():
        if ((a >= r[0] and a <= r[1]) or (a >= r[2] and a <= r[3])):
            return True
    return False

total = 0
invalid_index = []
for ind, n in enumerate(near):
    for j in n:
        if not check(j):
            invalid_index.append(ind)
            total += j
print(f'Part1:{total}')


columns = [None]*len(rules)
for r, n in enumerate(near):
    if r in invalid_index:
        continue
    for c, j in enumerate(n):
        if columns[c] is None:
            columns[c] = [j]
        else:
            columns[c].append(j)

def check_one(cols, r):
    counter = 0
    for a in cols:
        if ((a >= r[0] and a <= r[1]) or (a >= r[2] and a <= r[3])):
            counter += 1
    return counter

possible = [None]*len(rules)
for c, col in enumerate(columns):
    for r, rule in enumerate(rg):
        counter = check_one(col, rg[rule])
        if check_one(col, rg[rule]) != len(col):
            continue
        if possible[c] is None:
            possible[c] = set([rule])
        else:
            possible[c].add(rule)
            
soln = {}
while len(soln) < 20:
    for d, i in enumerate(possible):
        if len(i) != 1: continue
        cu = i - set(soln.values())
        soln[d] = list(cu)[0]
        for e in possible:
            if soln[d] in e:
                e.remove(soln[d])

prod = 1
for k,v in soln.items():
    if 'departure' in v:
        prod *= my[k]
print(f'Part2:{prod}')