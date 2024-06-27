n = int(input())
a = list(map(int, input().split()))
sorted_a =  sorted(list(set(a)))
print(sorted_a[-2])