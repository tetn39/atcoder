n, m, d = map(int, input().split())

a = list(set(map(int, input().split())))
b = list(set(map(int, input().split())))

a.sort()
b.sort()
if len(a) > len(b):
    temp = a
    a = b
    b = temp

def binary_search(value, ls):
    left = 0
    right = len(ls) - 1
    while left <= right:
        mid = (left + right) // 2
        if ls[mid] == value:
 
            return mid
        elif ls[mid] < value:
 
            left = mid + 1
        else:
 
            right = mid - 1

    return mid

# print(a)
# print(b)
ans = -1
for i in range(len(a)):
    saidai = a[i] + d
    bs = binary_search(saidai, b)
    # print(bs)
    if abs(b[bs] - a[i]) <= d:
        # print('a')
        ans = max(ans, a[i] + b[bs])
    elif abs(b[bs-1] - a[i]) <= d:
        # print('b')
        ans = max(ans, a[i] + b[bs-1])

print(ans)