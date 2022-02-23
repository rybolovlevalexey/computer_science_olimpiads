for i1 in range(1, 50):
    for i2 in range(1, 50):
        for i3 in range(1, 50):
            st = '0' + '1' * i1 + '2' * i2 + '3' * i3
            while '01' in st or '02' in st or '03' in st:
                st = st.replace('01', '210', 1)
                st = st.replace('02', '3101', 1)
                st = st.replace('03', '2302', 1)
            if st.count('1') == 52 and st.count('2') == 33 and st.count('3') == 23:
                print(i2)
