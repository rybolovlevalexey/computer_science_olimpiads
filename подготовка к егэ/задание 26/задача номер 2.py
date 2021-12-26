file = open('26_2.txt', 'r')
sp = file.read().strip().split('\n')
n, s = map(int, sp[0].split())
del sp[0]
summaA = 0
countB = 0
for i in range(len(sp)):
    elem = sp[i]
    if elem[-1] == 'B':
        continue
    money, colvo, tip = elem.split()
    money, colvo = int(money), int(colvo)
    summaA += money * colvo
print(summaA)
print(s > summaA)

sp = list(map(lambda elem: elem.split(), sp))
sp = sorted(sp, key=lambda x: int(x[0]))
summaB = 0
for i in range(len(sp)):
    elem = sp[i]
    if elem[-1] == 'A':
        continue
    money, colvo, tip = elem
    money, colvo = int(money), int(colvo)
    if summaA + summaB + money * colvo < s:
        countB += colvo
        summaB += money * colvo
    else:
        for j in range(colvo, 0, -1):
            if summaA + summaB + money * j < s:
                countB += j
                summaB += money * j
                break
print(countB, s - summaB - summaA)