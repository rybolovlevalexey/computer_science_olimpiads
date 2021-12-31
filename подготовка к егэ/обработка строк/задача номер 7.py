file = open('24-1.txt', 'r')
st = file.read().strip()
sp = list()
number_now = ''
for i in range(len(st)):
    elem = st[i]
    if ord('A') <= ord(elem) <= ord('Z') and number_now == '':
        continue
    elif ord('A') <= ord(elem) <= ord('Z') and number_now != '':
        sp.append(int(number_now))
        number_now = ''
    elif not ord('A') <= ord(elem) <= ord('Z'):
        number_now += elem
print(max(filter(lambda x: x % 2 == 0, sp)))
