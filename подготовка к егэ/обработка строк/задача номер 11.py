file = open('24-164.txt', 'r')
sp = file.read().strip().split('\n')
all_dlliny = list()
for s in sp:
    dlina = 1
    max_dlina = 0
    for j in range(1, len(s)):
        if s[j - 1] == s[j]:
            dlina += 1
        elif s[j - 1] != s[j]:
            if dlina > max_dlina:
                max_dlina = dlina
            dlina = 1
    if dlina > max_dlina:
        max_dlina = dlina
    all_dlliny.append(max_dlina)

ind = all_dlliny.index(max(all_dlliny))
st = sp[ind]
dic = dict()
for i in range(ord('A'), ord('Z') + 1):
    dic[chr(i)] = st.count(chr(i))
letter = min(dic, key=lambda x: dic[x])
print(letter, dic[letter])
