# https://atcoder.jp/contests/abc082/tasks/abc082_b
# diff: 497

s = list(input())
t = list(input())

s.sort()
t.sort(reverse=True)

ans = 'No'

if s < t:
    ans ='Yes'
print(ans)