n, m = map(int, input().split())
h = list(map(int, input().split()))


ans = 0
idx = 0
while m > 0 and idx < n:
    if m - h[idx] >= 0:
        m -= h[idx]
        idx += 1
        ans += 1
    else:
        break




print(ans)