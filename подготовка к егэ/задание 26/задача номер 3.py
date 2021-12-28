file = open('26_4.txt', 'r')
sp = file.read().strip().split('\n')
n = int(sp[0])
del sp[0]
for i in range(len(sp)):
    elem = sp[i]
    ryad, mesto = map(int, elem.split())
    sp[i] = [ryad, mesto]
sp = sorted(sp, key=lambda x: x[0], reverse=True)
dict_ryady = dict()
for elem in sp:
    ryad, mesto = elem
    if ryad in dict_ryady:
        dict_ryady[ryad] += [mesto]
    else:
        dict_ryady[ryad] = [mesto]
for key, value in dict_ryady.items():
    flag = True
    value = sorted(value)
    for i in range(len(value) - 1):
        if value[i] + 6 == value[i + 1]:
            print(value[i])
            print(key, value)
            flag = False
    if not flag:
        break
