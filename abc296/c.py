n, x = map(int, input().split())
a = set(map(int, input().split()))
ans = 'No'

for i in a:
    if i + x in a or i - x in a:
        ans = 'Yes'
        break

print(ans)