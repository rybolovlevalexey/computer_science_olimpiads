from fractions import Fraction

n = int(input())
ans = Fraction(0)
for i in range(1, n + 1):
    ans += Fraction(1, i**2)
print(ans)