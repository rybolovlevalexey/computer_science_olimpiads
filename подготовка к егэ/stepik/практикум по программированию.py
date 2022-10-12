dnk = {'g': 'c', 'c': 'g', 't': 'a', 'a': 'u'}
st = input()
ans = ''
for elem in st:
    ans += dnk[elem.lower()]
ans = ans.upper()
print(ans)