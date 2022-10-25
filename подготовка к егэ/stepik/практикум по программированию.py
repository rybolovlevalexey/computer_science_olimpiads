import random

n = 10**6
cnt = 0
for i in range(n):
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)
    if x**2 + y**2 <= 1:
        cnt += 1
s = (cnt / n) * 4
print(s)