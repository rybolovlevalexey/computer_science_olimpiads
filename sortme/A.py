n = int(input())
row = 0
delt = 1
while n > 0:
    row += 1
    n -= delt
    delt += 1
if n < 0:
    row -= 1
print(row)
