st = 39 * '1' + 39 * '2'
while '111' in st:
    st = st.replace('111', '2', 1)
    st = st.replace('222', '1', 1)
print(st)