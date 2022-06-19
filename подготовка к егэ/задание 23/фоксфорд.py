file = open('Zadanie-260283 (1).txt', 'r')

st = file.read().strip().split('F')
print(st.count('FF'))
mxdl = 0
for i in range(len(st) - 3):
    dl = len(st[i]) + len(st[i + 1]) + len(st[i + 2]) + len(st[i + 3]) + 3
    mxdl = max(mxdl, dl)
print(mxdl)