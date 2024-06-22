n = int(input())
d = list(map(int, input().split()))

ans = 0
for i in range(n):
    month = i+1

    for j in range(1, d[i]+1):
        if len(set(list(str(month)) + list(str(j)))) == 1:
            ans += 1
print(ans)
