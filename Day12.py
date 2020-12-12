data = open('./input.txt').read().splitlines()
data = list(map(lambda i: (i[0], int(i[1:])), data))

def turn(d,x,y,n):
    while n:
        if d == 'R':
            x, y = y, -x
        else:
            x, y = -y, x
        n -=1
    return (x,y)

dmap = {'E':(1,0), 'W':(-1,0), 'S':(0,-1), 'N':(0,1)}
move = lambda cur, pos, val: (cur[0]*val + pos[0], cur[1]*val + pos[1])

def solve(way, part):
    pos = (0,0)
    for dirn, val in data:
        if dirn == 'F':
            pos = move(way, pos, val)
        elif dirn in 'LR':
            way = turn(dirn, *way, val//90)
        else:
            if part == 1:
                pos = move(dmap[dirn], pos, val)
            else:
                way = move(dmap[dirn], way, val)
    return abs(pos[0]) + abs(pos[1])

print(solve(way = (1,0), part=1))
print(solve(way = (10,1), part=2))