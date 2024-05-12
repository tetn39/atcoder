n, k = map(int, input().split())
a = list(map(int, input().split()))

ans = 0
total = 0

for i in range(n):
    if k >= (total + a[i]):
        total += a[i]
    else:
        ans += 1
        total = a[i]

if total > 0:
    ans += 1

print(ans)