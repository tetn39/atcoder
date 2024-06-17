n = int(input())
a = list(map(int, input().split()))

ans = []

for i in range(1, n):

    if a[i-1] < a[i]:
        for j in range(a[i-1], a[i]):
            ans.append(j)
    else:
        for j in range(a[i-1], a[i], -1):
            ans.append(j)
ans.append(a[-1])
print(*ans)

# 1年前に書いた回答だからへんな書き方の可能性もある