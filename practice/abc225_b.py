n = int(input())
g = [[] for _ in range(n)]
ans = 'Yes'
for i in range(n-1):
    a, b = map(int, input().split())
    g[a-1].append(b-1)
    g[b-1].append(a-1)

for i in range(n):
    if not (len(g[i]) == 1 or len(g[i]) == n-1):
        ans = 'No'
        break

print(ans)