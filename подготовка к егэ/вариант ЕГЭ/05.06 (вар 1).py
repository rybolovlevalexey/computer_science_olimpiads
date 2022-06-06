st = 1000 * '9'
while '999' in st or '888' in st:
    if '888' in st:
        st = st.replace('888', '9', 1)
    else:
        st = st.replace('999', '8', 1)
print(st)