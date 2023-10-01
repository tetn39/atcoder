n, m = map(int, input().split())
s = input()
t = input()

ans = -1

settou = False
setubi = False

if t[:n] == s:
    settou = True

if t[-n:] == s:
    setubi = True


if settou and setubi:
    ans = 0
elif settou and not setubi:
    ans = 1
elif setubi and not settou:
    ans = 2
else:
    ans = 3

print(ans)
