# DABE
file = open('128009(1).txt', 'r')
st = file.read().strip()
n = 1
while st.count('DABE' * (n + 1)) >= 1:
    n += 1
print(n)
print(st.count('DABE' * 1 + 'DAB'))
