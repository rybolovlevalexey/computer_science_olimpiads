st = input()
for i in '.,!?:;-':
    st = st.replace(i + ' ', ' ')
    st = st.replace(i, ' ')
st = st.split()
words = dict()
for wor in st:
    if wor in words:
        words[wor] += 1
    else:
        words[wor] = 1
mn = None
ans = ''
for key, value in words.items():
    if mn is None or mn > value:
        mn = value
        ans = key
    if mn == value and ans > key:
        ans = key
print(ans)