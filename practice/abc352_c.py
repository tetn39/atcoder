n = int(input())

body = 0
max_head = 0
for i in range(n):
    a, b = map(int, input().split())
    body += a
    head = b - a
    max_head = max(head, max_head)

ans = body + max_head
print(ans)
