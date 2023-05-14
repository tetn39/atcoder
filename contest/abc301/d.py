s = list(input())
n = int(input())
kouho = []

# ?を0として考え、現在の値を算出する

defa = 0
big_defa = 0
for i in range(1, len(s)+1):
    if s[-i] == '?':
        num = 0
        num2 = 1 * (2**(i-1))
        kouho.append(num2)
    else:
        num = int(s[-i]) * (2**(i-1))
        num2 = num
    defa += num
    big_defa += num2


if n < defa:
    print(-1)
    quit()


# defaとnとの差を求め、その差以下のkouhoから大きい順に入れる。そしてその差をまた調べ、kouhoから選び入れていく

sa = n - defa
kouho.sort(reverse=True)

for i in range(len(kouho)):
    if kouho[i] <= sa:
        defa += kouho[i]
        sa -= kouho[i]



print(defa)

