from collections import defaultdict

defa = defaultdict(int)

n = int(input())

for i in range(n):
    s = input()
    defa[i] = s.count('o')


ans = []
for i in range(n, -1, -1):
    for j in range(n):
        if defa[j] == i:
            ans.append(j+1)

print(*ans)

        