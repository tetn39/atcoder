# https://atcoder.jp/contests/abc171/tasks/abc171_d
# diff: 498

from collections import Counter
n = int(input())
de = Counter(map(int, input().split()))
q = int(input())
ans = 0

for i in de.keys():
    ans += de[i]*i

for i in range(q):
    b, c = map(int, input().split())
    sa = c - b
    ans += sa * de[b]
    de[c] += de[b]
    de[b] = 0

    print(ans)





# TLE
from collections import defaultdict
n = int(input())
a = list(map(int, input().split()))
q = int(input())

de = defaultdict(int)
for i in a:
    de[i] += 1




for i in range(q):
    ans = 0
    b, c = map(int ,input().split())
    de[c] += de[b]
    de[b] = 0

    for j in de.keys():
        ans += de[j]*j
    print(ans)
