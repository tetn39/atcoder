s = input()
lower = 0
upper = 0
for i in range(len(s)):
    x = s[i]
    if x.islower():
        lower += 1
    else:
        upper += 1

if lower < upper:
    print(s.upper())
else:
    print(s.lower())