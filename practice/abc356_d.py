n, m = map(int, input().split())

max_bit = 60
MOD = 998244353
ans = 0
n1 = n+1
m_bit = str(bin(m)[2:])
m_bit = m_bit.zfill(max_bit)
# print(m_bit)

for i in range(60):
    if m_bit[-(i+1)] == '1':

        bit = 2**i
        wari = n1 // bit
        amari = n1 % bit

        # 奇数ならa
        if wari % 2:
            ans += bit * (wari // 2)
            ans += amari
        else:
            ans += bit * (wari // 2)
            
        ans %= MOD
    else:
        continue
print(ans)