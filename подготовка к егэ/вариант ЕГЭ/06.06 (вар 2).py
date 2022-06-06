sp = ['м', 'а', 'т', 'в', 'е', 'й']
ans = 0

for i1 in sp:
    for i2 in sp:
        for i3 in sp:
            for i4 in sp:
                for i5 in sp:
                    for i6 in sp:
                        st = i1 + i2 + i3 + i4 + i5 + i6
                        if len(set(st)) == 6 and i1 != 'й' and st.count('ае') == 0:
                            ans += 1
print(ans)