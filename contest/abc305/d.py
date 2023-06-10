n = int(input())
a = list(map(int, input().split()))
q = int(input())

def binary_search(ls, value):
    left = 0
    right = len(ls) - 1
    while left <= right:
        mid = (left + right) // 2
        if ls[mid] == value:
 
            return mid
        elif ls[mid] < value:
 
            left = mid + 1
        else:
 
            right = mid - 1

    return mid

for i in range(q):
    l, r = map(int, input().split())
    ans = 0
    ans_ = [0]
    gosa_l = 0
    gosa_r = 0

    bs_l = binary_search(a, l)
    bs_r = binary_search(a, r)
    # print(bs_l)
    # print(bs_r)
    atokara = True
    if l > a[bs_l]:
        atokara = False
        bs_l += 1
    
    # rは大きくても増やしても増やさなくても寝てる時間は変わらないためよい

    # 次に寝てる時間の合計
    suimin = False
    for j in range(bs_l, bs_r+1):
        # 偶数なら
        if j % 2 != 0:
            # 寝始めた
            suimin = True
            continue
        
        
        if suimin:
            # 起きたので
            suimin = False
            # print(j)
            ans_.append(a[j] - a[j-1])
            ans += a[j] - a[j-1]

    # lの足すぶん
    if atokara:
        ans_.append(a[bs_l] - l)
        # ans -= l - a[bs_l-2]

    # rのひくぶん
    if bs_r % 2 == 0:
        if r > a[bs_r]:
            pass
        else:

            ans_.append(r - a[bs_r])
        # ans += r - a[bs_r-1]


    print(ans_)
    print(sum(ans_))
    print('------------------------')