n = int(input())
st_x = input()
st_y = input()

ax = int(st_x.replace('-', '+').split('+')[0])
bx = int(st_x.replace('-', '+').split('+')[1][:-1])
zx = st_x[len(str(ax))]
if zx == '-':
    bx *= (-1)
ay = int(st_y.replace('-', '+').split('+')[0])
by = int(st_y.replace('-', '+').split('+')[1][:-1])
zy = st_y[len(str(ay))]
if zy == '-1':
    by *= (-1)
aans = 0
bans = 0

a = ax
b = bx
for i in range(n - 1):
    a = a * ax - b * bx
    b = b * ax + a * bx
aans += a
bans += b

a = ay
b = by
for i in range(n - 1):
    a = a * ay - b * by
    b = b * ay + a * by
aans += a
bans += b

a = ax
b = (-1) * bx
for i in range(n - 1):
    a = a * ax + b * bx
    b = (-1) * b * ax - a * bx
aans += a
bans += b

a = ay
b = (-1) * by
for i in range(n):
    a = a * ay + b * by
    b = (-1) * b * ay - a * by
aans += a
bans += b
if b > 0:
    print(f'({a}+{b}j)')
elif b == 0:
    print(f'({a})')
else:
    print(f'({a}{b}j)')