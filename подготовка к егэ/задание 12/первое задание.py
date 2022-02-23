st = '>' + '1' * 20 + '2' * 20 + '3' * 20
while '>1' in st or '>2' in st or '>3' in st:
    st = st.replace('>1', '22>3', 1)
    st = st.replace('>2', '33>', 1)
    st = st.replace('>3', '11>2', 1)
print(st)
print(sum(map(int, list(st[:-1]))))