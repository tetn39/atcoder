# https://atcoder.jp/contests/abc325/tasks/abc325_c
from collections import deque
h, w = map(int, input().split())

s = [list(input()) for _ in range(h)]
q = deque()
visited = [[False] * w for _ in range(h)]
graph = [[[] for _ in range(w)] for _ in range(h)]



def dfs(x):

    q.append(x)
    while q:
        v1, v2 = q.pop()
        if not visited[v1][v2]:
            visited[v1][v2] = True
            for u1, u2 in graph[v1][v2]:
                if not visited[u1][u2]:
                    q.append((u1, u2))



# 移動方向 上から時計回り 
dirc = [(-1, 0),(-1, 1),(0, 1),(1, 1),(1, 0),(1, -1),(0, -1),(-1, -1)] 
for i in range(h):
    for j in range(w):

        if s[i][j] == '.':
            continue
        else:
            for di, dj in dirc:
                ni, nj = i + di, j + dj
                if 0 <= ni < h and 0 <= nj < w and s[ni][nj] == '#':
                    graph[i][j].append((ni, nj))
                    # graph[ni][nj].append((i, j)) # どうせ逆からもやるので入れない

ans = 0
for i in range(h):
    for j in range(w):
        if s[i][j] == '#':
            if visited[i][j]:
                continue
            dfs((i, j))
            ans += 1

print(ans)