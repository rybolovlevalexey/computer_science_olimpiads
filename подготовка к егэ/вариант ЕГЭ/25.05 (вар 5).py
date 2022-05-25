letter = 'L'
file = open('zadanie24_2 (1).txt', 'r')
st = file.read().strip()
dl = 0
mxdl = 0

for i in range(0, len(st)):
    if st[i] == letter:
        dl += 1
    else:
        if dl > mxdl:
            mxdl = dl
        if st[i] == 'L':
            dl = 1
        else:
            dl = 0

    if letter == 'L':
        letter = 'D'
    elif letter == 'D':
        letter = 'R'
    else:
        letter = 'L'

print(dl)
print(mxdl)
print(st.count('LDR' * 5 + 'L'))
print(st[st.index('LDR' * 5):st.index('LDR' * 5) + 16])