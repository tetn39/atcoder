x, y = map(int, input().split())

ans = 'No'

if x-3 <= y <= x+2:
    ans = 'Yes'

print(ans)