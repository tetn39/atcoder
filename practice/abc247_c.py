n = int(input())

dic = {0:[]}

for i in range(1, 17):
    dic[i] = dic[i-1] + [i] + dic[i-1]

print(*dic[n])