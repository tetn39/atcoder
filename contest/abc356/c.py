n, m, k = map(int, input().split())

n += 1
bit_ls = []
hantei = []
for b in range(2 ** (n - 1)):
    bit = bin(b)[2:].zfill(n - 1)
    bit_ls.append(list(str(bit)))
    hantei.append(0)
# print(bit_ls)
ans = 0
c_ls = []
a_ls = []
r_ls = []
for i in range(m):
    x = list(input().split())
    c_ls.append(x[0])
    a_ls.append(x[1:-1])
    r_ls.append(x[-1])

for bit in bit_ls:

    cnt = 0
    for i in range(m):
        a = a_ls[i]
        r = r_ls[i]
        c = c_ls[i]
        
        sum_a = 0
        for j in range(int(c)):
            x = int(a[j])-1
            if bit[x] == "1":
                sum_a += 1
        
        if sum_a >= k:
            if r == "o":
                cnt += 1
        else:
            if r == "x":
                cnt += 1
    if cnt == m:
        ans += 1

print(ans)