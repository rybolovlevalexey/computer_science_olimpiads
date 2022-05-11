st = 156 * '8'
while '77' in st or '888' in st:
    if '77' in st:
        st = st.replace('77', '88', 1)
    else:
        st = st.replace('888', '7', 1)
print(st)