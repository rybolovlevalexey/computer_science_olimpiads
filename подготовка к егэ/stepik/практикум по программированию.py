st = input()
for elem in '.,;:-?!':
    st = st.replace(elem, ' ')
while '  ' in st:
    st = st.replace('  ', ' ')
print(len(set(map(lambda x: x.lower(), st.split()))))