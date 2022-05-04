st = 121 * '563'
while '56' in st or '3333' in st:
    st = st.replace('56', '3', 1)
    st = st.replace('3333', '3', 1)
print(st)