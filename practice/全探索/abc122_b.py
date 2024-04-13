s = input()

ACGT = ["A","C","G","T"]

ans = 0
ans_max = 0
for i in s:
    if i in ACGT:
        ans_max += 1
    else:
        ans = max(ans_max, ans)
        ans_max = 0
ans = max(ans_max, ans)
print(ans)