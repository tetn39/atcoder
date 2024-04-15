from collections import defaultdict
n = int(input())

defa = defaultdict(int)
for i in range(n):
    yum, color = map(int, input().split())
    if defa[color] == 0:
        defa[color] = yum
    else:
        defa[color] = min(defa[color], yum)

print(max(defa.values()))