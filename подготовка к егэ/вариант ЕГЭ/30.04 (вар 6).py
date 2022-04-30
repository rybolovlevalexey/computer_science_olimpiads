st = 54 * '5' + '7'
while '722' in st or '557' in st:
    if '722' in st:
        st = st.replace('722', '57', 1)
    else:
        st = st.replace('557', '72', 1)
print(st)