n = int(input())
a = list(map(int, input().split()))

if sorted(a) == list(range(1, n+1)):
    print('Yes')
else:
    print('No')
