from decimal import *
num = Decimal(input())
res = num.exp() + num.ln() + num.log10() + num.sqrt()
print(res)