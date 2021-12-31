file = open('24-3.txt', 'r')
st = file.read().strip()
lenght = 1
maximum = 0
for i in range(1, len(st)):
    if st[i - 1] < st[i]:
        lenght += 1
    elif st[i - 1] >= st[i]:
        if maximum < lenght:
            maximum = lenght
            lenght = 0
if lenght > maximum:
    print(lenght)
else:
    print(maximum)