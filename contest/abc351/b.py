n = int(input())

a_ = []
b_ = []
for i in range(n):
    a_.append(input())
for i in range(n):
    b_.append(input())


for i in range(n):
    for j in range(n):
        if a_[i][j] != b_[i][j]:
            print(i+1, j+1)
