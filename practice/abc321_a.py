n = list(input())

ans = 'No'
tmp = 10
for i in range(len(n)):
    if int(n[i]) < tmp:
        tmp = int(n[i])
    else:
        break
else:
    ans = 'Yes'

print(ans)