from collections import defaultdict
n, t = map(int, input().split())
a = list(map(int, input().split()))
yoko = defaultdict(int)
tate = defaultdict(int)
naname1 = 0
naname2 = 0


ans = -1
for i in range(t):
    x = a[i]-1
    row = x // n
    column = x % n

    yoko[row] += 1
    tate[column] += 1
 
    if row == column:
        naname1 += 1
    
    if row == n - column - 1:
        naname2 += 1
    
    if yoko[row] == n or tate[column] == n or naname1 == n or naname2 == n:
        ans = i+1
        break

print(ans)