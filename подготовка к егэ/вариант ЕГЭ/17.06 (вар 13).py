file = open('zadanie24_1.txt', 'r')
st = file.read().strip()
n = 1
while st.count('AB' * (n + 1)) >= 1:
    n += 1
print(n)
print(st.count('AB' * 12))