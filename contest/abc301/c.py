from collections import defaultdict, Counter
s = input()
t = input()
de = defaultdict(int)
atcoder = ['a', 't', 'c', 'o', 'd', 'e', 'r']

#　メモ
# 数がすべて同じになればいい
# @の数だけ譲歩できる
# 違いの数と、@の数を調べる

cos = Counter(s)
cot = Counter(t)

ham = 0
jo = 0

jo += cos['@']
jo += cot['@']
flag = True

for i in cos.keys():
    if i == '@':
        continue
    sa = abs(cos[i] - cot[i])
    if 0 < sa:
        if i not in atcoder:
            flag = False
    ham += sa

ans_1 = False
if flag:
    if ham <= jo:
        ans_1 = True


ham = 0
jo = 0

jo += cos['@']
jo += cot['@']
flag = True

for i in cot.keys():
    if i == '@':
        continue
    sa = abs(cos[i] - cot[i])
    if 0 < sa:
        if i not in atcoder:
            flag = False
    ham += sa

ans_2 = False
if flag:
    if ham <= jo:
        ans_2 = True


if ans_1 and ans_2:
    print('Yes')
else:
    print('No')

