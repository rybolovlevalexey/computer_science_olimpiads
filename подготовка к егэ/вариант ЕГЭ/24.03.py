st = '1' + '9' * 98
while '19' in st or '299' in st or '3999' in st:
    st = st.replace('19', '2', 1)
    st = st.replace('299', '3', 1)
    st = st.replace('3999', '1', 1)
print(st)