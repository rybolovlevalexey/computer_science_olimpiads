cnt = 0
sp = ['з', 'и', 'м', 'а']
for i1 in sp:
    for i2 in sp:
        for i3 in sp:
            for i4 in sp:
                for i5 in sp:
                    st = i1 + i2 + i3 + i4 + i5
                    if (st.count('и') == 1 and st.count('а') == 0) or (st.count('и') == 0 and st.count('а') == 1):
                        cnt += 1
print(cnt)