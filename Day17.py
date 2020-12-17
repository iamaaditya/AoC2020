from itertools import product

data = '''....#...
.#..###.
.#.#.###
.#....#.
...#.#.#
#.......
##....#.
.##..#.#'''

#part = (0,) # For part1
part = (0, 0) # For part2

directions = [i for i in product([-1,0,1], repeat=2+len(part)) if i!=(0,0,*part)]          
neigh = lambda k: [tuple([i+j for i,j in zip(k, s)]) for s in directions]

def rule(points, k):
    count = sum([i in points for i in neigh(k)])
    if k in points and count in [2, 3]: return True
    if k not in points and count == 3: return True
    return False
    
points = set()
for i, row in enumerate(data.splitlines()):
    for j, val in enumerate(list(row)):
        if val == '#': points.add((i, j, *part))

for i in range(6):
    updates = set()
    for x in set([n for k in points for n in neigh(k) + [k]]):
        if rule(points, x): updates.add(x)
    points = updates

print(len(points))

