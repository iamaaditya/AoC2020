data = open('./input.txt').read().splitlines()

def update(v, mask, part2=True):
    c = '0' if part2 else 'X'
    value = list(format(v, '#038b')[2:])
    for i, j in enumerate(mask):
        if j == c: continue
        value[i] = j
    return ''.join(value)

def get_all_add(mask):
    x_ind = [i for i,v in enumerate(mask) if v == 'X']
    add = []
    for i in product(*repeat([0,1], len(x_ind))):
        current = list(mask)
        for j, c in zip(x_ind, i):
            current[j] = str(c)
        add.append(int(''.join(current), 2))
    return add

def solve(part2=True):
    mask, ans = None, {}
    p = re.compile('\[(\d*)\] = (\d*)')
    for line in data:
        if line.startswith('mask'):
            mask = line.split('=')[1].strip()
        else:
            address, value = map(int, re.findall(p, line)[0])
            if part2:
                add_x = update(address, mask)
                for new_add in get_all_add(add_x):
                    ans[new_add] = value
            else:
                ans[address] = int(update(value, mask, part2=part2), 2)
    return sum(ans.values())

print(solve(part2=False))
print(solve(part2=True))