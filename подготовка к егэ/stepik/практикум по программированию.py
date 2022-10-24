a = int(input())
b = int(input())
for num in range(a, b + 1):
    sp = list()
    for d in str(num):
        if d == '0':
            sp.append(False)
        else:
            sp.append(num % int(d) == 0)
    if all(sp):
        print(num, end=' ')
