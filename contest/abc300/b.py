h, w = map(int, input().split())

a = [list(input()) for _ in range(h)]
b = [list(input()) for _ in range(h)]


# print(a)
for i in range(h):
    

    for k in range(w):
        for j in range(h):
            a[j] = a[j][1:] + [a[j][0]]   
        # print(a)
        if a == b:
            print('Yes')
            quit()
    a = a[1:] + [a[0]]

print('No')
            
