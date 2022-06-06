# XZZY
file = open('24 (3).txt', 'r')
st = file.read().strip()
sp = st.split('XZZY')
dliny = list()
for i in range(len(sp)):
    dliny.append(len(sp[i]))
print(dliny)
dlina = max(dliny)
dlina += 3
dlina += 3
print(dlina)