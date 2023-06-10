p, q = input().split()

ls = [3, 1, 4, 1, 5, 9]
al = ['A', 'B', 'C', 'D', 'E', 'F', 'G']

p = al.index(p)
q = al.index(q)



print(sum(ls[min(p, q):max(p, q)]))