from fractions import Fraction

def prost(x, y):
    if max(x, y) % min(x, y) == 0 and min(x, y) != 1:
        return False
    for d in range(2, min(x, y) // 2 + 1):
        if x % d == 0 and y % d == 0:
            return False
    return True

n = int(input())
for ch in range(n - 1, 0, -1):
    zn = n - ch
    if ch > zn:
        continue
    if prost(zn, ch):
        print(Fraction(ch, zn))
        break