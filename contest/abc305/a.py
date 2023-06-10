n = int(input())

ue = int(n/5+0.9) * 5

sita = int(n/5) * 5

# print(ue)
# print(sita)

if abs(n-ue) < abs(n-sita):
    print(ue)
else:
    print(sita)