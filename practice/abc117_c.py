def input_n():
    n = int(input())
    return n


def input_s():
    s = input()
    return s
def input_s_list(n):
    s = [input() for _ in range(n)]
    return s

def input_nm():
    n, m = map(int, input().split())
    return n, m
def input_list():
    n = list(map(int, input().split()))
    return n


n, m = input_nm()
x = input_list()
x.sort()
# if n >= m:
#     print(0)
#     exit()
sa = []
ans = 0
for i in range(1, m):
    sa.append(x[i] - x[i-1])
sa.sort()
print(sa)
ans = sum(sa[:len(sa)-(n-1)])
print(ans)

