n = int(input())
s = input()
ans = ''

for i in range(len(s)):
    ans += f'{s[i]}'*2

print(ans)

