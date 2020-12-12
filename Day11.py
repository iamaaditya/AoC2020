from itertools import product

def neigh(row,col, part2=True):
    out = []
    for (i,j) in product((-1,0,1), (-1,0,1)):
        if not i and not j: continue
        r,c = row,col
        while not (r+i)//row_len and not (c+j)//col_len:
            if d[r+i][c+j] == '.' and part2:
                r+=i
                c+=j
            else:
                out.append((r+i, c+j))
                break
    return [d[i][j] for i,j in out]

def solve(part2):
    while True:
        updates = []
        for (i,j) in product(range(row_len), range(col_len)):
            occu = sum([1 for k in neigh(i,j, part2=part2) if k == '#'])
            if d[i][j] == 'L' and occu == 0:
                updates.append((i,j,'#'))
            if d[i][j] == '#' and occu >= 4 + int(part2):
                updates.append((i,j,'L'))
        if len(updates) == 0:
            break
        for i,j,c in updates:
            d[i][j] = c            
    return sum([1 for i in range(mr) for j in range(mc) if d[i][j]=='#'])

for part2 in [False, True]:
    d = [list(i) for i in open('input.txt').read().splitlines()]
    print(solve(part2=part2))
