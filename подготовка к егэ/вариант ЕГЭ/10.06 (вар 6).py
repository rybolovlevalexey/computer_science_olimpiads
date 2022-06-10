file = open('107_24.txt', 'r')
st = file.read().strip()
cnt = 0
mxcnt = 0
i = 0

while i < len(st) - 1:
    if (st[i] == 'A' and st[i + 1] == 'B') or (st[i] == 'C' and st[i + 1] == 'B'):
        i += 2
        cnt += 1
    else:
        if cnt > mxcnt:
            mxcnt = cnt
        cnt = 0
        i += 1
print(mxcnt)
print(cnt)