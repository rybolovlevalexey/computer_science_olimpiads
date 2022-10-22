n = int(input())
sp = list()
for i in range(n):
    sp.append(list(map(int, input().split('.'))))

print(*map(lambda x: '.'.join(map(lambda y: str(y), x)), sorted(sp, key=lambda x: x[0] * 256**3 + x[1] * 256**2 + x[2] * 256 + x[3])), sep='\n')
