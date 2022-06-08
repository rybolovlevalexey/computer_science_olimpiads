ans = list()
sp = ['а', 'б', 'в', 'г', 'д']
for i1 in sp[1:]:
    for i2 in sp:
        for i3 in sp:
            for i4 in sp:
                for i5 in sp:
                    st = i1 + i2 + i3 + i4 + i5
                    if st.count('аа') == 0 and st.count('бб') == 0 and st.count('вв') == 0 and st.count('гг') == 0 and st.count('дд') == 0:
                        ans.append(st)
print(len(ans))