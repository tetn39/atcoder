from decimal import Decimal
a, b = map(Decimal, input().split())

print(int((a/b) + Decimal(0.999999999)))