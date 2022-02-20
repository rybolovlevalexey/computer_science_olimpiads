st = '219' * 219
while '21' in st or '9999' in st:
    st = st.replace('21', '9', 1)
    st = st.replace('9999', '9', 1)
print(st)
