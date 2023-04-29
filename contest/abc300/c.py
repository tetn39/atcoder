# 途中まで できてない

from collections import defaultdict
h, w = map(int, input().split())

c = [list(input()) for _ in range(h)]

de = defaultdict(bool)
count = defaultdict(int)

for i in range(h):
    for j in range(w):
        flag = True
        
        if c[i][j] == '#':
            flag = True
            co = 1
            if de[i, j] == False:
                de[i, j] = True
                while flag:
                    if i+1 > h-1 or j+1 > w-1:
                        # flag = False
                        break

                    if c[i+1][j+1] != '#' or de[i+1, j+1]: # 右下が#じゃない or 右下がいったことある
                        # flag = False
                        break
                    co += 1
                    i += 1
                    j += 1
                    de[i, j] = True

                print(co)
                print(i, j)
                if co > 1:
                    print('aaa')
                    print(i, j)
                    count[int((co-1)/2)] += 1
        

print(count)
