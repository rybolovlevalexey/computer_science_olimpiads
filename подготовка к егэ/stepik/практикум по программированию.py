from fractions import Fraction

def prost(x, y):
    if max(x, y) % min(x, y) == 0 and min(x, y) != 1:
        return False
    for d in range(2, min(x, y) // 2 + 1):
        if x % d == 0 and y % d == 0:
            return False
    return True

n = int(input())
ans = list()
for zn in range(2, n + 1):
    for ch in range(1, zn):
        if prost(zn, ch):
            ans.append(Fraction(ch, zn))
print(*sorted(ans), sep='\n')