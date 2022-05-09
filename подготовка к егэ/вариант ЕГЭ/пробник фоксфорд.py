def is_prost(x):
    for d in range(2, int(x ** 0.5) + 1):
        if x % d == 0:
            return False
    return True


file = open('Zadanie-273978_A.txt', 'r')
sp = list(map(int, file.read().strip().split('\n')))
n = sp[0]
del sp[0]
prostye = [0] * n
for i in range(len(sp)):
    if is_prost(sp[i]):
        prostye[i] = 1
indexes = list()
for i in range(len(prostye)):
    if prostye[i] == 1:
        indexes.append(i)
print(indexes)
i1 = 0

mxsm = 0
while i1 + 2 <= 6:
    i2 = i1 + 2
    summa = sum(sp[i1: i2])
    if summa > mxsm:
        mxsm = summa
    i1 += 1
print(mxsm)
print(sum(sp))
print(sum(sp[31:]))