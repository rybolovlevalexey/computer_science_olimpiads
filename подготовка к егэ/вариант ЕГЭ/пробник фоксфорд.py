st = 110 * '6' + 23 * '5'
while '6666' in st or '5555' in st:
    if '6666' in st:
        st = st.replace('6666', '55', 1)
    if '5555' in st:
        st = st.replace('5555', '66', 1)
print(st)