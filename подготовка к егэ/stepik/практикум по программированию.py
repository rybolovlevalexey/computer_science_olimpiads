m = int(input())
n = int(input())
math = set()
inf = set()
for i in range(m):
    math.add(input())
for i in range(n):
    inf.add(input())
res = len(math) + len(inf) - 2 * len(math & inf)
print(math, inf)
print(math & inf)
if res == 0:
    print('NO')
else:
    print(res)