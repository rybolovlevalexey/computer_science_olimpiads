file = open('24 (2).txt', 'r')
st = file.read().strip()
letters = dict()
for i in range(2, len(st)):
    if st[i - 1] == st[i - 2]:
        if st[i] in letters:
            letters[st[i]] += 1
        else:
            letters[st[i]] = 1
print(max(letters))
print(len(letters))
rever = {value: key for key, value in letters.items()}
print(rever)
print(len(rever))
print(max(rever.keys()))
print(rever[1547])