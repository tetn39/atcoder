n = int(input())
s = input()

t = 0
a = 0
for i in range(n):
    if s[i] == 'T':
        t += 1
    else:
        a += 1

if t < a:
    print('A')
elif a < t:
    print('T')
else:
    ha = t
    t = 0
    a = 0
    for i in range(n):
        if s[i] == 'T':
            t += 1
        else:
            a += 1

        if t == ha:
            print('T')
            quit()
        if a == ha:
            print('A')
            quit()