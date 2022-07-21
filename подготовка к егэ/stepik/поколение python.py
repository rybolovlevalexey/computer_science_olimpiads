flag = False
st = input()
sp = list(st)
newsp = list()
for i in range(len(sp)):
    if 97 <= ord(sp[i]) <= 122:
        newsp.append(sp[i])
for i in range(len(newsp)):
    sp1 = newsp[:i] + newsp[i + 1:]
    if sp1 == sp1[::-1]:
        print('True')
        flag = True
        break
if not flag:
    print('False')
