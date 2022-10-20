from fractions import Fraction

m = (input())
n = (input())
print(f'{m} + {n} = {Fraction(m) + Fraction(n)}')
print(f'{m} - {n} = {Fraction(m) - Fraction(n)}')
print(f'{m} * {n} = {Fraction(m) * Fraction(n)}')
print(f'{m} / {n} = {Fraction(m) / Fraction(n)}')
