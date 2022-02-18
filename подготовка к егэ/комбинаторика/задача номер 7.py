sp = ['к', 'р', 'ы', 'ш', 'а']
glas = ['ы', 'а']
sogl = ['к', 'р', 'ш']
ans = set()
for i1 in sp:
    for i2 in sp:
        for i3 in sp:
            for i4 in sp + ['']:
                for i5 in sp + ['']:
                    st = i1 + i2 + i3 + i4 + i5
                    flag = True
                    for i in st[1:]:
                        if i in sogl:
                            flag = False
                            break
                    if st.count('ы') <= 2 and st.count('а') <= 2 and flag:
                        ans.add(st)
print(len(ans))
