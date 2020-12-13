file = open('input.txt').read().splitlines()
start = int(file[0])
data = file[1].split(',')
times = [(index, int(time)) for index, time in enumerate(data) if time != 'x']

# Part 1
soln, smallest = 0, sys.maxsize
for index, time in times:
    gap = time - (start - start//time*time)
    if gap < smallest:
        smallest = gap
        soln = smallest * time
print(soln)

# Part 2
soln, increment = times[0]
for index, time in times[1:]:
    gap = time - (index % time)
    while True:
        if soln % time == gap:
            break
        soln += increment
    increment *= time
print(soln)

# Part 2 with CRT

from itertools import count
from functools import reduce

def inv_mod(Ni, b):
    # Solve: Ni * x = 1 (mod b)
    for i in count(1):
        if (Ni*i) % b == 1:
            return i

def crt(mods, remainders):
    N = reduce(lambda x, y: x * y, mods)
    ans = 0
    for b, n in zip(mods, remainders):
        Ni = N//b
        inv = inv_mod(Ni, b)
        ans += n * inv * Ni
    return ans % N

mods, remainders = zip(*[(time, time-i) for i, time in times])
print(crt(mods, remainders))