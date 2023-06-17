a = list(map(int, input().split()))
ans = 0

for i, n in enumerate(a):
   ans += n * (2**i)

print(ans)
