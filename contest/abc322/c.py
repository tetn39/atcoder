n, m = map(int, input().split())
a = list(map(int, input().split()))

index = 0
ans = -1
for i in range(n):
    if a[index] - (i+1) == 0:
        index += 1
        ans = 0
    else:
        ans = a[index] - (i+1)
    
    print(ans)