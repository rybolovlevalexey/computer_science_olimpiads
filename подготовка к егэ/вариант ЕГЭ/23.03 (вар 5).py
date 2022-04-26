cnt = 0
sp = ['л', 'е', 'в', 'и', 'й']
for i1 in sp:
    for i2 in sp:
        for i3 in sp:
            for i4 in sp:
                for i5 in sp:
                    st = i1 + i2 + i3 + i4 + i5
                    if st.count('л') == 1 and st.count('е') == 1 and st.count('в') == 1 and \
                            st.count('и') == 1 and st.count('й') == 1 and st[0] != 'й' and \
                            st.count('еи') == 0:
                        cnt += 1
print(cnt)