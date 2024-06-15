n = int(input())
ans = 0
bin_n = str(bin(n))[2:][::-1]
ans = bin_n.find('1')
print(ans)