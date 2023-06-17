from collections import defaultdict
n = int(input())
a = list(map(int, input().split()))

defa = defaultdict(int)
# defa2 = defaultdict(int)
ans = []


for i in range(n*3):
    if defa[a[i]] == 1:
        defa[a[i]] += 1
        ans.append(a[i])
        # defa2[a[i]] = i+1

    else:
        defa[a[i]] += 1



# print(defa2)
print(*ans)
