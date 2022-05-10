st = 84 * '1'
while '11111' in st:
    st = st.replace('222', '1', 1)
    st = st.replace('111', '2', 1)
print(st)