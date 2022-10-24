import math

num = int(input())
func = input()
answer = {'квадрат': lambda x: x**2, 'куб': lambda x: x**3, 'корень': lambda x: x**0.5,
          'модуль': lambda x: abs(x), 'синус': lambda x: math.sin(x)}
print(answer[func](num))