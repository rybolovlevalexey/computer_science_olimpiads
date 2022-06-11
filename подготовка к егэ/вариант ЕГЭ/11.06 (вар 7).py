file = open("27880.txt", 'r')
sp = file.read().strip().split('\n')
s, n = map(int, sp[0].split())
del sp[0]
sp = list(sorted(map(int, sp)))
summa = 0
cnt = 0
lstelem = 0
for elem in sp:
    if elem + summa <= s:
        summa += elem
        cnt += 1
        lstelem = elem
    else:
        break
print(cnt)
summa -= lstelem
print(lstelem, summa, s)
for elem in sp[::-1]:
    if summa + elem <= s:
        print(elem)
        break