n, x = map(int, input().split())
alp = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ') # このアルファベットは出力例1からコピペ
n_alp = ''
for i in range(26):
    n_alp += alp[i] * n

print(n_alp[x-1])