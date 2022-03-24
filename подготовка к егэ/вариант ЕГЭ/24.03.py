sp = ['б', 'о', 'р', 'и', 'с']
ans = 0
for i1 in sp:
    for i2 in sp:
        for i3 in sp:
            for i4 in sp:
                for i5 in sp:
                    for i6 in sp:
                        st = i1 + i2 + i3 + i4 + i5 + i6
                        if st.count('б') == 1 and st.count('р') == 1 and (st.count('с') == 1 or st.count('с') == 0):
                            ans += 1
print(ans)