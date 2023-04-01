al = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
al.reverse()
ans = ''
for i in range(8):
    s = input()
    if not '*' in s:
        continue
    
    for n, j in enumerate(s):
        if j == '*':
            ans += al[7-n]
    ans += str(8-i)

print(ans)

