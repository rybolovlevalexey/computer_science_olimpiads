st = input()
while '  ' in st:
    st = st.replace('  ', ' ')
let = dict()
for elem in st.split():
    if elem in let:
        let[elem] += 1
    else:
        let[elem] = 1
    print(let[elem], end=' ')