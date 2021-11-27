sp = ['э', 'т', 'а', 'н']
ans = 0
for a1 in sp:
    for a2 in sp:
        for a3 in sp:
            for a4 in sp:
                for a5 in sp:
                    st = a1+a2+a3+a4+a5
                    if st.count('э') + st.count('а') == 1:
                        ans += 1
print(ans)