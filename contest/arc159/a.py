# 未完成

from collections import defaultdict
from collections import deque

n, k = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
q = int(input())

graph = defaultdict(list)
for i in range(n):
    for j in range(n):
        if a[i][j] == 1:
            graph[i].append(j)

print(graph) #TODO
 
for i in range(q):
    s, t = map(lambda j: (int(j)-1)%n, input().split())

    # print(s, t) #TODO

    que = deque()
    que.append(graph[s]) # 例: 0, 1, 2
    ans = 0
    hantei = defaultdict(bool)
    flag = True

    while que and flag:
        x = que.popleft()
        print(x)
        # ゴールか判定
        for j in x:
            if j == t:
                flag = False
                break
            
            # xが2回目にならないように
            # いった場所か判定（終わりを見つけるのがメイン）
            if hantei[j]:
                continue

            hantei[j] = True

        # 次のqueについか
        for j in x:
            que.append(j) # 例：[1] [1] がqueに追加される

        print(ans)
        ans += 1
        print(que)
    print(ans)



"""
Kは何回繰り返すか、みたいな感じ
NをK回繰り返す

aは0, 1である

1, 4ははみ出た 4%3 の１を見て判断
sは縦、（行）
tは横、（列）で見る　（％する）

x は現在の位置
自分も行けるグラフなので、すでにいったところか判断するdefaultdictも必要


3 2
1 1 1
1 1 0
0 1 0
4
6 3



1 2
1 4
1 6
5 4
"""