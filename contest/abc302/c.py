import itertools
n, m = map(int, input().split())
s = [list(input()) for _ in range(n)]

a = (list(itertools.permutations(s)))
ans = 'No'
for i in range(len(a)):
    x = a[i]
    for j in range(n-1):
        hami = 0
        for k in range(m):
            if x[j][k] != x[j+1][k]:
                hami += 1
        if hami != 1:
            break
    else:
        print('Yes')
        quit()


print(ans)
