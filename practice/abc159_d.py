# https://atcoder.jp/contests/abc159/tasks/abc159_d
# diff: 496

import math
from collections import Counter
n = int(input())
a = list(map(int, input().split()))
co = Counter(a)
base = 0
ans = 0
for i in co:
    base += math.comb(co[i], 2)



for i in range(n):
    x = a[i]
    xc = math.comb(co[x], 2)
    xc_ = math.comb(co[x]-1, 2)
    sa = xc - xc_
    ans = base - sa

    print(ans)