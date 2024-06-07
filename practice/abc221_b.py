s = input()
t = input()

sa = 0
sa_idx = []
s_txt = []
t_txt = []
if s == t:
    print('Yes')
    quit()
for i in range(len(s)):
    if s[i] != t[i]:
        sa += 1
        s_txt.append(s[i])
        t_txt.append(t[i])
        sa_idx.append(i)

if sa == 2 and sa_idx[1]-sa_idx[0] == 1 and t_txt[0] == s_txt[1] and t_txt[1] == s_txt[0]:
    print('Yes')
else:
    print('No')