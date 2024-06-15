ls = list(map(int, input().split()))

ans = 'No'
cnt = 0
for i in ls:
    cnt += ls.count(i)

if cnt == 13:
    ans = 'Yes'

print(ans)