st = '>' + '1'*30 + '2'*20 + '3'*10
while '>1' in st or '>2' in st or '>3' in st:
    st = st.replace('>1', '2>3', 1)
    st = st.replace('>2', '33>', 1)
    st = st.replace('>3', '1>22', 1)
print(st.count('1') + st.count('2') * 2 + st.count('3') * 3)
st = st[:st.index('>')] + st[st.index('>') + 1:]
print(sum(map(int, list(st))))
