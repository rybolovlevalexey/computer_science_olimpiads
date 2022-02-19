ans = set()
sp = ['c', 'о', 'л', 'о', 'в', 'е', 'й']
for i1 in sp:
    for i2 in sp:
        for i3 in sp:
            for i4 in sp:
                for i5 in sp:
                    for i6 in sp:
                        st = i1 + i2 + i3 + i4 + i5 + i6
                        if st.count('й') <= 1 and i1 != 'й' and i6 != 'й':
                            if 'й' in st:
                                ind = st.index('й')
                                if st[ind - 1] != 'е' and st[ind + 1] != 'е':
                                    ans.add(st)
                            elif 'й' not in st:
                                ans.add(st)
print(len(ans))