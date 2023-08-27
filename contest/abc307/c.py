from collections import defaultdict
n = int(input())
a = list(map(int, input().split()))

for i in range(n):
    a[i] -= 1

defa = defaultdict(int)
ed = defaultdict(bool)


for i in range(n):
    defa[i] = a[i]

# print(defa)


ans_n = 0
ans_ls = []
ans_temp = 0
for i in range(n):
    flag = True
    if ed[i]:
        continue
    
    now = i
    graph_in = defaultdict(bool)
    while flag:
        if graph_in[now]:
            ans_temp = now
            break

        next = a[now]
        if ed[next]:
            flag = False
            break
        graph_in[now] = True
        now = next
            

    
    if flag:
        break

# print(ans_temp)
# print(a)
now = ans_temp
while True:
    ans_ls.append(now+1)

    next = a[now]

    if next == ans_temp:
        break
    
    now = next

ans_n = len(ans_ls)
print(ans_n)
print(*ans_ls)