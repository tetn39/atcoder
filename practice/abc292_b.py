n, q = map(int, input().split())

dic = {i:0 for i in range(1, n+1)}
for i in range(q):
    score, player = map(int, input().split())
    if score == 3:
        if dic[player] >= 2:
            print('Yes')
        else:
            print('No')
    else:
        dic[player] += score
    