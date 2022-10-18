from decimal import *
num = Decimal(input())
print(num.as_tuple().digits)
if num >= 1:
    print(max(num.as_tuple().digits) + min(num.as_tuple().digits))
else:
    print(max(num.as_tuple().digits))