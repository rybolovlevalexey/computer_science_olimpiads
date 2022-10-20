from fractions import Fraction

def fack(x):
    res = 1
    for j in range(1, x + 1):
        res *= j
    return res
n = int(input())
ans = Fraction(0)
for i in range(1, n + 1):
    ans += Fraction(1, fack(i))
print(ans)