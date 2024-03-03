s = input()

a = []
for i in s[1::2]:
    a.append(i)
#     print(i)

# print(a)
if "1" in a:
    print('No')
else:
    print('Yes')