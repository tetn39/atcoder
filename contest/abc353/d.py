from collections import defaultdict
n = int(input())
a = list(map(int, input().split()))
ans = 0
waru = 998244353
defa = defaultdict(int)
for i in range(n-1, -1, -1):
    if i != 0:
        ans += (a[i]*i)
    
    defa[i] = 10 ** (len(str(a[i]))) + defa[i+1] 
    ans += defa[i+1] * a[i]


print(ans % waru)