n, m = map(int, input().split())
dic = {}
a = list(map(int, input().split()))
for i in range(m):
    dic[i] = a[i]


for i in range(n):
    x = list(map(int, input().split()))
    for j in range(m):
        dic[j] -= x[j]

for i in range(m):
    if dic[i] > 0:
        print('No')
        exit()
print('Yes')