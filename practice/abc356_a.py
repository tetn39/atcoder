n, l, r = map(int, input().split())
a = list(range(1, n+1))
a2 = a.copy()
for i in range(l-1, r):
    a[i] = a2[r-i+l-2]

print(*a)