st = '>' + 11 * '1' + 12 * '2' + 30 * '3'
while '>1' in st or '>2' in st or '>3' in st:
    if '>1' in st:
        st = st.replace('>1', '22>', 1)
    if '>2' in st:
        st = st.replace('>2', '222>', 1)
    if '>3' in st:
        st = st.replace('>3', '1>', 1)
print(st.count('2') * 2 + st.count('1'))