for i in range(91, 120):
    st = '1' * i
    while '111' in st:
        st = st.replace('111', '2', 1)
        st = st.replace('2222', '333', 1)
        st = st.replace('33', '1', 1)
    print(i, st)
