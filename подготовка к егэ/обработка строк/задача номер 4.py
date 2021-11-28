file = open('24_3.txt', 'r')
text = file.read().strip()
sp = list()
for i in range(len(text)):
    elem = text[i]
    if elem == 'Z':
        sp.append(i)
start = 0
finish = 4
ans = -1

while finish < len(sp):
    i1 = sp[start]
    i2 = sp[finish]
    delta = abs(i1 - i2) - 1
    if ans == -1 or delta > ans:
        ans = delta
    start += 1
    finish += 1
print(ans)