sp = set()
for i in range(128, 256):
    n = i
    n = bin(n)[2:]
    n = list(n)
    n[1], n[2] = n[2], n[1]
    n[2], n[3] = n[3], n[2]
    n = ''.join(n)
    n = int(n, 2)
    n -= i
    sp.add(n)
print(sp)
print(max(sp))