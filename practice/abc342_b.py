n = int(input())
p = list(map(int, input().split()))
q = int(input())


for i in range(q):
    a, b = map(int, input().split())
    ans = -1
    if p.index(a) < p.index(b):
        ans = a 
    else:
        ans = b 

    print(ans)
