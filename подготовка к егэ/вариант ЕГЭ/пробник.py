a = list('ababbababbaa')
q = 1
i = 1
while q < 4:
    c = a[i - 1]
    if q == 2:
        if c == 'a':
            a[i - 1] = 'b'
        else:
            q = 1
    if q == 3:
        if c == 'b':
            a[i - 1] = 'a'
        else:
            q = 1
    if q == 1:
        del a[i - 1]
        i = i - 1
        if c == 'a':
            q = 3
        if c == 'b':
            q = 2
    i += 1
    if i > len(a):
        q = 4
print(''.join(a))