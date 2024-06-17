s = [input() for _ in range(10)]

start_i, start_j, end_i, end_j = 0, 0, 0, 0
start_flag, end_flag = True, True
for i in range(10):
    for j in range(10):
        if s[i][j] == '#' and start_flag:
            start_i = i
            start_j = j
            start_flag = False
            
        if s[9-i][9-j] == '#' and end_flag:
            end_i = 9-i
            end_j = 9-j
            end_flag = False

print(start_i+1, end_i+1)
print(start_j+1, end_j+1)