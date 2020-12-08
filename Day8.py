data = [(i.split()[0], int(i.split()[1])) for i in open('./input.txt').read().splitlines()]

def ends(data, part1 = False):
    visited = [False]*len(data)
    total, index = 0, 0
    while True:
        if index >= len(data):
            break
        if visited[index]:
            return total if part1 else False
        else:
            visited[index] = True
        if data[index][0] == 'acc': 
            total += data[index][1]
        if data[index][0] == 'jmp':
            index += data[index][1]
            continue
        index += 1
    return total


print('Part1: ' + str(ends(data, part1=True)))

for i,d in enumerate(data):
    if d[0] == 'acc': continue
    data[i] = ('jmp', d[1]) if d[0] == 'nop' else ('nop', d[1])
    total =  ends(data)
    if total:
        break
    data[i] = d # restore the original
    
print(total)