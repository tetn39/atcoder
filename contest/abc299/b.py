n, t = map(int, input().split())
c = list(map(int, input().split()))
r = list(map(int, input().split()))
ans = 0
if t in c:
    for i in range(n):
        if c[i] == t:
            if ans < r[i]:
                ans = r[i]

else:
    color = c[0]
    for i in range(n):
        if c[i] == color:
            if ans < r[i]:
                ans = r[i]

print(r.index(ans)+1)