f = list(map(int, open('input.txt').read().splitlines()))

def isvalid(arr, num):
        arr_map = set(arr)
        for i in arr:
            if num-i != i and num-i in arr:
                return True
        return False

pre=25
for i,j in enumerate(range(pre, len(f))):
    if not isvalid(f[i:j], f[j]):
        target = f[j]
        break
print(f'Part1: {target}')

# O(N^2)
start=0
end = 1
while True:
    current = f[start:end]
    if sum(current) == target:
        print(min(current) + max(current))
        break
    elif sum(current) > target:
        start +=1
        end = start + 1
        continue
    end += 1

# O(N)
start = 0
end = 1
current_sum = f[0] 
while end <= len(f): 
    while current_sum > target and start < end-1: 
        current_sum = current_sum - f[start] 
        start += 1
    if current_sum == target: 
        print(min(f[start:end-1]) + max(f[start:end-1]))
        break
    current_sum = current_sum + f[end] 
    end += 1