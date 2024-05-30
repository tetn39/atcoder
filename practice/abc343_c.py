n = int(input())
ls = []
tmp = 0
x = 0
while n > x:
    x = tmp ** 3
    ls.append(x)
    tmp += 1
for i in range(len(ls)-1, -1, -1):
    if n >= ls[i]:
        num1 = str(ls[i])
        num2 = str(ls[i])[::-1]
        if num1 == num2:
            print(num1)
            break


