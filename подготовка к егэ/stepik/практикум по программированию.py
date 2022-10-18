import random
sp = set()
while len(sp) < 100:
    ans = str(random.randint(1, 9))
    for j in range(6):
        ans += str(random.randint(0, 9))
    sp.add(ans)
print(*sp, sep='\n')
