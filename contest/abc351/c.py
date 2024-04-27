from collections import deque
n = int(input())
a = deque(map(int, input().split()))

qu = deque()


for i in range(n):
    x = a.popleft()
    qu.append(x)
    while len(qu) >= 2:
        if qu[-1] != qu[-2]:
            break
        else:
            tmp = qu.pop()
            qu.pop()
            qu.append(tmp+1)


print(len(qu))