n = int(input())
a = list(map(int, input().split()))
dic = {}
for i in range(n):
    x = a[i]
    if x == -1:
        dic[0] = i+1
    else:
        dic[x] = i+1

# print(dic)
ans = []
root = 0
for _ in range(n):
    x = dic[root]
    ans.append(x)
    root = x

print(*ans)