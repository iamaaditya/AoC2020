data = list(map(int,open('input.txt').read().splitlines()))

d = [0] + sorted(data) + [max(data) + 3]

cur = 0
diff = {i:0 for i in range(4)}
for i in sorted(data):
    if i <= cur + 3:
        chain.append(i)
        diff[i-cur]+=1
        cur = i
print(diff[1] *(diff[3]+1))     
    

memo = {}
for i in d:
    memo[i] = 0
    for j in range(1,3+1):
        if i-j in memo:
            memo[i-j] += 1
memo[d[-1]] = 1

for j in range(len(d)-2, -1, -1):
    memo[d[j]] = sum([memo[d[j+s]] for s in range(1,memo[d[j]]+1)])
    
print(memo[0])    