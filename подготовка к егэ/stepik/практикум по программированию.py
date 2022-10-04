n = int(input())
for i in range(n):
    st = list()
    for j in range(n):
        if i == j or i == n - 1 - j or j == n // 2 or i == n // 2:
            st.append("*")
        else:
            st.append(".")
    print(*st, sep=' ')
