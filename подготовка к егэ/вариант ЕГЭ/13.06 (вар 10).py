file = open('zadanie24_2 (2).txt', 'r')
st = file.read().strip()
n = 1
while True:
    if st.count('LDR'*n) == 0:
        break
    n += 1
print(st.count('LDR' * 5))