forbidden_words = open('forbidden_words.txt')
bad_words = list(map(lambda x: x.strip(), forbidden_words.read().split()))
name = input()
file = open(name)
oldst = file.read()
st = oldst.lower()
for elem in bad_words:
    st = st.replace(elem, '*' * len(elem))
ans = ''
for i in range(len(oldst)):
    if st[i] == '*':
        ans += st[i]
    else:
        ans += oldst[i]
print(ans)