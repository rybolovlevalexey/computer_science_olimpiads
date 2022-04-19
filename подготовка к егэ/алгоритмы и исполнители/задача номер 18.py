st = '4' * 123
while '4444' in st or '7777' in st:
    if '4444' in st:
        st = st.replace('4444', '77', 1)
    else:
        st = st.replace('7777', '44', 1)
print(st)