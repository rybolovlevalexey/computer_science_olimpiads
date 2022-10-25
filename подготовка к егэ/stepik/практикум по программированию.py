file = open('goats.txt')
output = open('answer.txt', 'w')
colors = set()
file.readline()
goats = dict()
flag = False
cnt = 0
for elem in file.readlines():
    elem = elem.strip()
    if elem == 'GOATS':
        flag = True
        continue
    if not flag:
        colors.add(elem.split()[0])
        goats[elem.split()[0]] = 0
    else:
        goats[elem.split()[0]] += 1
    if flag:
        cnt += 1
ans = list()
for key, value in goats.items():
    if value / cnt > 0.07:
        ans.append(f'{key} goat')
ans = sorted(ans)
output.write('\n'.join(ans))
output.close()