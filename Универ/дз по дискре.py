import fractions
p1 = fractions.Fraction(1, 13) * 10
for i in range(9):
    num = fractions.Fraction(48 - i, 51 - i)
    p1 *= num

p2 = fractions.Fraction(1, 13) * fractions.Fraction(1, 17) * 45
for i in range(8):
    num = fractions.Fraction(48 - i, 50 - i)
    p2 *= num

p3 = fractions.Fraction(1, 13) * fractions.Fraction(1, 17) * fractions.Fraction(1, 25) * 120
for i in range(7):
    num = fractions.Fraction(48 - i, 49 - i)
    p3 *= num

p4 = fractions.Fraction(1, 13) * fractions.Fraction(1, 17) * fractions.Fraction(1, 25) * 210
p4 *= fractions.Fraction(1, 49)

print(p1, p2, p3, p4)
print(p1, 2*p2, 3*p3, 4*p4)
ans = p1 + 2*p2 + 3*p3 + 4*p4
print(ans)

ans2 = p1 + 4*p2 + 9*p3 + 16*p4
print(ans2)
res = ans2 - ans*ans
print(res)