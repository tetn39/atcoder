# https://atcoder.jp/contests/abc347/submissions/52418554
n, a, b = map(int, input().split())
d = list(map(int, input().split()))
week = a + b
e = []
for i in d:
    # e.append(min(abs(week-i), i % week))
    if i % week == 0:
        e.append(week)
    else:
        e.append(i % week)
# print(week)
# print(a)
# print(e)
kyori = []
day_max = max(e)
day_min = min(e)
sa = day_max - day_min
right = [0]
left = [0]
for i in range(n):
    if abs(week-e[i]) < e[i]:
        right.append(week-e[i])
    else:
        left.append(e[i])


left_max = max(left)
right_max = max(right)
sa2 = left_max + right_max


judge = min(sa, sa2)

if judge >= a:
    print("No")
else:
    print("Yes")


"""error
2 3 4
6 8

3 3 4
11 13 15 

2 3 4
7 8


無理パターン
3 3 4
5 8 11"""