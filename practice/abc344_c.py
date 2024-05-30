from collections import defaultdict

defa = defaultdict(bool)

n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))
l = int(input())
c = list(map(int, input().split()))
q = int(input())
x = list(map(int, input().split()))

for i in range(n):
    for j in range(m):
        for k in range(l):
            defa[a[i] + b[j] + c[k]] = True

for i in range(q):
    if defa[x[i]]:
        print('Yes')
    else:
        print('No')