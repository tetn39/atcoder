n, m = map(int, input().split())
s = [input() for _ in range(n)]
ans = n
for i in range(2**n):
    bit = bin(i)[2:].zfill(n)
    ls = [1] * m
    
    for j in range(n):
        if bit[j] == '1':
            for k in range(m):
                if s[j][k] == 'o':
                    ls[k] = 0


    if sum(ls) == 0:
        ans = min(ans, bit.count('1'))
    
print(ans)