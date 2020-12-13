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