s1 = input()
s2 = input()
s3 = input()
t = list(map(int, input()))
s = [s1, s2, s3]
ans = ""
for i in t:
    ans += s[i-1]

print(ans)