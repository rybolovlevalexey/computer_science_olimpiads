def evaluate(coefficients, x):
    ans = 0
    i = len(coefficients) - 1
    for elem in coefficients:
        ans += elem * x**i
        i -= 1
    return ans


coef = list(map(int, input().split()))
x = int(input())
print(evaluate(coef, x))