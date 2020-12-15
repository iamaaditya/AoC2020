#input, end = [0, 3, 6], 2020 # ans:436
#input, end = [0,1,4,13,15,12,16], 2020 # ans:1665
input, end  = [0,1,4,13,15,12,16], 30000000 # ans:16439

s = {j:[i] for i,j in enumerate(input, start=1)}

start, prev = True, input[-1]
for i in range(len(input)+1, end+1):
    if prev not in s or start:
        if 0 not in s:
            s[0] = [i]
            start = True
        else:
            s[0].append(i)
            start = False
        prev = 0        
    else:
        prev = s[prev][-1] - s[prev][-2]
        if prev in s:
            s[prev].append(i)
        else:
            s[prev] = [i]
            start = True
print(prev)