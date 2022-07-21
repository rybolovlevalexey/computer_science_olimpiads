sostnow = 0
ans = list()
st = input()
i = 0
while i < len(st):
    if st[i] == '|':
        ans.append(1)
        i += 2
    else:
        ans.append(0)
        i += 1
print(''.join(list(map(str, ans))))