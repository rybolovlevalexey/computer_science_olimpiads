file = open('nums.txt')
sp = file.readlines()
if len(sp) > 1:
    nums = list()
    for elem in sp:
        elem = elem.strip()
        try:
            elem = int(elem)
            nums.append(elem)
        except Exception:
            continue
    print(sum(nums))
else:
    st = sp[0].strip()
    while '  ' in st:
        st = st.replace('  ', ' ')
    a, b = map(int, st.split())
    print(a + b)