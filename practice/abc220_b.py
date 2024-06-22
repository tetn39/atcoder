k = int(input())
a, b = input().split()

ans = 0
ak = 0
bk = 0
a = a[::-1]
b = b[::-1]
for i in range(len(a)):
    ak += int(a[i]) * (k**i)

for i in range(len(b)):
    bk += int(b[i]) * (k**i)

ans = ak * bk
print(ans)
