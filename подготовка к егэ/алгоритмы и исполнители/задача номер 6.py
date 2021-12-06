st = '1' * 2020 + '2' * 2020

while '11111' in st:
    if '222' in st:
        ind = st.index('222')
        st = list(st)
        for i in range(2):
            del st[ind]
        st[ind] = '1'
        st = ''.join(st)
    if '111' in st:
        ind = st.index('111')
        st = list(st)
        for i in range(2):
            del st[ind]
        st[ind] = '2'
        st = ''.join(st)
print(st)