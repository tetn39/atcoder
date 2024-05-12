from collections import defaultdict
n = int(input())
a = list(map(int, input().split()))
a.sort()
# print(a)
ans = 0
waru = 10 ** 8
defa = defaultdict(int) 
mainasu = 0
half = waru // 2
half_i = -1
target_i = 0
kore = True
for i in range(n):
    if a[i] >= half:
        if half_i == -1:
            half_i = i
            target_i = i
        
        if kore:
            for j in range(target_i-1, -1, -1):
                if waru > a[i] + a[j]:
                    mainasu += (half_i - target_i)
                    break
                else:
                    target_i = j
        if target_i == 0:
            kore = False

        if kore == False:
            mainasu += half_i



        mainasu += (i - half_i)
    ans += a[i] * (n-1)

# print(ans)
# print(mainasu)
print(ans - (mainasu*waru))