sp = ['и', 'в', 'а', 'н']
ans = 0
for i1 in sp:
    for i2 in sp:
        for i3 in sp:
            for i4 in sp:
                for i5 in sp:
                    st = i1 + i2 + i3 + i4 + i5
                    if st.count('и') >= 1:
                        ans += 1
print(ans)