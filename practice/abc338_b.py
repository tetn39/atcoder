from collections import Counter
s = list(input())
count = Counter(s)
ans = ''
target = max(count.values())
for key in sorted(count.keys()):
    if count[key] == target:
        ans = key
        break

print(ans)