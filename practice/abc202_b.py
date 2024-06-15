s = input()

oomoji = False
komoji = False
kotonaru = True
ls = []

for i in s:
    if i.isupper():
        oomoji = True
    elif i.islower():
        komoji = True

    ls.append(i)

if len(ls) != len(set(ls)):
    kotonaru = False

if oomoji and komoji and kotonaru:
    print('Yes')
else:
    print('No')