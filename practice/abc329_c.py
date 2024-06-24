from collections import defaultdict

n = int(input())
s = input()
longest_al = {}
ans = 0

tmp = ''
cnt = 0
for i in range(n):
    x = s[i]
    if tmp != x:
        longest_al[tmp] = max(longest_al.get(tmp, 0), cnt)
        tmp = x
        cnt = 1
    else:
        cnt += 1

longest_al[tmp] = max(longest_al.get(tmp, 0), cnt)

for nx in longest_al:
    ans += longest_al[nx]

print(ans)