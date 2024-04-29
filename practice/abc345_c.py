from collections import Counter

s = input()
count = Counter(s)
c = []
ans = 0
for i in count.values():
    c.append(i)
    if i > 1:
        ans = 1


for i in range(len(c)):
    for j in range(i+1, len(c)):
        ans += c[i] * c[j]

print(ans)