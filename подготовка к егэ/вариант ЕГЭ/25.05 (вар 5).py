file = open('27-B (1).txt', 'r')
sp = file.read().strip().split('\n')
n = int(sp[0])
del sp[0]
summa = 0
chet = 0
nechet = 0
delts = list()

mndl_notequal = None

for elem in sp:
    a, b = map(int, elem.split())
    summa += min(a, b)
    delts.append(abs(a - b))
    if min(a, b) % 2 == 0:
        chet += 1
    else:
        nechet += 1
    if a % 2 != b % 2 and (mndl_notequal is None or mndl_notequal > abs(a - b)) and abs(a - b) != 27:
        mndl_notequal = abs(a - b)
    if abs(a - b) == 27 or abs(a - b) == 47 or abs(a - b) == 100 or abs(a - b) == 101 or abs(a - b) == 102 or abs(a - b) == 103:
        print(a, b, 'a and b', abs(a - b))

print(summa)
print(chet, nechet)
print(sorted(delts))
print(min(delts))
print()
print(mndl_notequal)