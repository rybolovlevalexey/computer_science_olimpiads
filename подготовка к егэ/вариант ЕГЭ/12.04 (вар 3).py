file = open('26_demo.txt', 'r')
sp = file.read().strip().split('\n')
s, n = map(int, sp[0].split())  # свободное место на диске/количество пользователей
del sp[0]
summa = 0
cnt = 0
last_elem = -1
sp = sorted(map(int, sp))
for elem in sp:
    if summa + elem > s:
        break
    else:
        summa += elem
        cnt += 1
        last_elem = elem
print(summa, cnt)  # 8176  568
print(last_elem)  # 29
summa = summa - last_elem
for i in range(567, n):
    if summa + sp[i] > s:
        print(sp[i - 1])
        break
print(summa + sp[i - 1])
print(sp[i])