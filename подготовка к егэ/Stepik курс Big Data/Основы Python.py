x = int(input())
n = int(input())
sp = list()
for i in range(n):
    st = list(map(int, input().split()))
    sp.append(st)
matrix = list()
for i in range(n):
    st = list()
    for j in range(n):
        st.append(sp[j][i])
    matrix.append(st)
for elem in matrix:
    if x in elem:
        print('YES')
    else:
        print('NO')