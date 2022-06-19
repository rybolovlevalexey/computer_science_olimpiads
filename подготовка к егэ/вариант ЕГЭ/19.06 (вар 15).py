st = '1' + 99 * '8' + '1'
while '81' in st or '882' in st or '8883' in st:
    if '81' in st:
        st = st.replace('81', '2', 1)
    elif '882' in st:
        st = st.replace('882', '3', 1)
    else:
        st = st.replace('8883', '1', 1)
print(st)