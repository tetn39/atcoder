n = int(input())
s = input()
ans = -1

if 'o' not in s or '-' not in s:
    print(ans)
    quit()

ren = 0
for i in range(n):
    if s[i] == 'o':
        ren += 1
    else:
        ans = max(ren, ans)
        ren = 0

print(max(ren, ans))