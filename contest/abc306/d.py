# 最終(エラー出る)
# これが一番正解に近い気がする
from collections import defaultdict
n = int(input())

ans = 0
x = []
y = []
kouho = []
kouho0 = []
for i in range(n):
    x_, y_ = map(int, input().split())

    if x_ == 0:
        if len(y) == 0:
            y.append(0)
        kouho.append(max(y))
        y = []
        kouho0.append(y_)
    else:
        y.append(y_)


temp = []
get = 0
temp.append(kouho0[0] + kouho[0])
for i in range(1, len(kouho)):
    temp.append(kouho0[i] + kouho[get:i+1])
    if temp[i] <= temp[i-1]:
        get = i
        ans += temp[i-1]
        temp[i] = (kouho0[i] + kouho[get:i+1])

if get != i:
    ans += temp[i]


if y:
    if max(y) > 0:
        ans += max(y)

print(ans)




# 途中（いわゆるdp）

from collections import defaultdict
n = int(input())

ans = 0
x = []
y = []
kouho = []
kouho0 = []
for i in range(n):
    x_, y_ = map(int, input().split())

    if x_ == 0:
        if len(y) == 0:
            y.append(0)
        kouho.append(max(y))
        y = []
        kouho0.append(y_)
    else:
        y.append(y_)


test = []
get = 0
# dp = [0] * n
dp = defaultdict(int)
dp[0] = max(0, kouho[0] + kouho0[0])
for i in range(1, len(kouho)):
    check = kouho0[i]
    saidai = max(kouho[get:i+1])
    if saidai + check > 0:
        if dp[i-1] < kouho0[i] + max(kouho[get:i+1]):
            dp[i] = max(dp[i-1], kouho0[i] + max(kouho[get:i+1]))
            ans += dp[i]
        else:
            get = i
            dp[i] = max(dp[i], kouho0[i]+kouho[i]) 
        # ans += (saidai + check)
        # test.append((saidai + check))

if dp[i] > 0:
    ans += dp[i]
if y: # yに残ってるなら
    if max(y) > 0:
        ans += max(y)


print(ans)