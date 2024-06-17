n, d = map(int, input().split())
t = list(map(int, input().split()))

ans = -1
total = 0
for i in range(1, n):
    if t[i] - t[i-1] <= d:
        ans = t[i]
        break

print(ans)