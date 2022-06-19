# DABE
file = open('Zadanie_24_text_dlia_KR_2(2).txt', 'r')
st = file.read().strip()
letd = dict()
letters = set(st)
for let in letters:
    for i in range(1, 10000):
        if st.count(let * i) > 0:
            letd[let] = i
for key, value in letd.items():
    if value == max(letd.values()):
        print(key)
print(letd)
print(letd['1'])