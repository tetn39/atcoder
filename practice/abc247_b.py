n = int(input())

ls = []
name_list = []
ans = 'Yes'
for i in range(n):
    s,t = input().split()
    name_list.append((s, t))
    ls.append(s)
    ls.append(t)

for i in range(n):
    x, y = name_list[i]
    if x == y:
        m = 1
    else:
        m = 0
    
    if ls.count(x)-m >= 2 and ls.count(y)-m >= 2:
        ans = 'No'
        break

print(ans)