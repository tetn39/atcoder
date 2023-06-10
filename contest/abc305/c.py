from collections import defaultdict
h,w = map(int, input().split())

s = [list(input()) for _ in range(h)]

# print(s)
tate = 0
# tate_ = []
yoko = 0
# yoko_ = []
yoko_ = defaultdict(int)
tate_ = defaultdict(int)
for i in range(h):
    # yoko_.append(s[i].count('#'))
    for j in range(w):
        if s[i][j] == '#':
            yoko_[i] += 1
            tate_[j] += 1

# print(yoko_)
# print(tate_)

h_ans = min(yoko_.values())
w_ans = min(tate_.values())

# print(h_ans)
# print(w_ans)
ans = []
for i in yoko_:
    if yoko_[i] == h_ans:
        ans.append(i+1)

for i in tate_:
    if tate_[i] == w_ans:
        ans.append(i+1)
    
print(*ans)