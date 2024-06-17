n = int(input())

dic = {}
for i in range(n):
    s, t = input().split()
    dic[int(t)] = s
target = sorted(dic.keys(), reverse=True)[1]
print(dic[target])
