s = input()
check_A = False
check_B = False
check_C = False

ans = 'Yes'
for i in range(len(s)):
    if s[i] == 'A':
        check_A = True
        if check_B or check_C:
            ans = 'No'
            break

    if s[i] == 'B':
        check_B = True
        if check_C:
            ans = 'No'
            break
    
    if s[i] == 'C':
        check_C = True
    
    

print(ans)