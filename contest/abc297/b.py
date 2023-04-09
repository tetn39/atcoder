s = input()

bflag = False
kflag = False


b = s.find('B')
br = s.rfind('B')

if b % 2 != br % 2:
    bflag = True

k = s.find('R')
kr = s.rfind('R')

r = s.find('K')

if k < r < kr:
    kflag = True

# print(bflag)
# print(kflag)

if kflag and bflag:
    print('Yes')
else:
    print('No')