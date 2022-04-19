for i1 in range(20):
    for i2 in range(20):
        for i3 in range(20):
            st = '0' + '1'*i1 + '2'*i2 + '3'*i3
            while '01' in st or '02' in st or '03' in st:
                st = st.replace('01', '310', 1)
                st = st.replace('02', '1201', 1)
                st = st.replace('03', '3022', 1)

            if st.count('1') == 59 and st.count('2') == 25 and st.count('3') == 42:
                print(i1, i2, i3)
                print(i1)
