n = int(input())
k = int(input())
sp = list(i for i in range(1, n + 1))
n = 1
while len(sp) > 1:
    ind = 0
    while ind < len(sp) and len(sp) > 1:
        if n % k == 0:
            del sp[ind]
        print(sp, n)
        ind += 1
        n += 1
print(*sp)