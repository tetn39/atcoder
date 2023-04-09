h, w = map(int, input().split())

for i in range(h):
    s = input()
    
    ans = []
    p_flag = False
    for j in range(w):
        if s[j] == '.':
            # 1コマがTかどうか
            if p_flag:
                ans.append('T')
                p_flag = False

            ans.append('.')
            continue
        
        # 2つ目のTなら
        if s[j] == 'T' and p_flag:
            ans.append('P')
            ans.append('C')
            p_flag = False
            continue

        elif p_flag: # 2個目がTじゃないなら
            ans.append('T')
            ans.append('T')
            p_flag = False
            continue

        if s[j] == 'T': # 繰り越し
            p_flag = True
    if p_flag:
        ans.append('T')

    print(''.join(ans))