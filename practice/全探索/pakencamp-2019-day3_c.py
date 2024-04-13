n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
ans = 0

for i in range(m):
    for j in range(i+1, m):
        total = 0
        for k in range(n):
            total += max(a[k][i], a[k][j])
        
        ans = max(ans, total)

print(ans)