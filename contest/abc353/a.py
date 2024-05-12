n = int(input())
h = list(map(int, input().split()))

ans = -1

target = h[0]

for i in range(1, n):
    if h[i] > target:
        target = h[i]
        ans = i + 1
        break

print(ans)
