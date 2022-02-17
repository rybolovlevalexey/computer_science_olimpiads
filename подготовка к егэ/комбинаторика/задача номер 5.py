ans = 0
sp = ['С', 'Ч', 'И', 'Т', 'А', 'Й']
for i1 in sp:
    for i2 in sp:
        for i3 in sp:
            for i4 in sp:
                st = i1 + i2 + i3 + i4
                if st.count('А') <= 1:
                    ans += 1
print(ans)
