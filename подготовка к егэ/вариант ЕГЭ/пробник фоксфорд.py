sp = ['к', 'а', 'с', 'т']
cnt = 0
for i1 in sp:
    for i2 in sp:
        for i3 in sp:
            for i4 in sp:
                for i5 in sp:
                    st = i1 + i2 + i3 + i4 + i5
                    if st.count('к') == 1 or st.count('к') == 2:
                        cnt += 1
print(cnt)
