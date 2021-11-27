sp = sorted(['и', 'н', 'с', 'т', 'а', 'в', 'к'])
glas = sorted(['и', 'а'])
sogl = sorted(['н', 'с', 'т', 'в', 'к'])
num = 1
for a1 in sogl:
    for a2 in sp:
        for a3 in sp:
            for a4 in glas:
                st = a1 + a2 + a3 + a4
                if st == 'ника':
                    print(num)
                    break
                num += 1