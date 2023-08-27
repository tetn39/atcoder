from collections import defaultdict
n, d = map(int, input().split())
defa = defaultdict(int)

for i in range(n):
    s = list(input())
    for j in range(len(s)):
        # ダメな日+=1
        if s[j] == 'x':
            defa[j] += 1


# print(defa)
        
ans = 0
temp = 0
for i in range(d):
    if defa[i] == 0:
        temp += 1
    else:
        ans = max(ans, temp)
        temp = 0

if defa[d-1] == 0:
    ans = max(ans, temp)
print(ans)