cnt = 0
for i1 in [1, 2, 3, 4]:
    for i2 in [1, 2, 3, 4]:
        for i3 in [1, 2, 3, 4]:
            for i4 in [1, 2, 3, 4]:
                for i5 in [1, 2, 3, 4]:
                    st = str(i1) + str(i2) + str(i3) + str(i4) + str(i5)
                    if st.count('1') == 2:
                        cnt += 1
print(cnt)