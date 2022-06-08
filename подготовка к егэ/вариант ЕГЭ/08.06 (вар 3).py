st = '1' + 80 * '8'
while ('18' in st) or ('288' in st) or ('3888' in st):
    if '18' in st:
        st = st.replace('18', '2', 1)
    elif '288' in st:
        st = st.replace('288', '3', 1)
    else:
        st = st.replace('3888', '1', 1)
print(st)