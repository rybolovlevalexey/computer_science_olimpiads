n = int(input())
for i in range(n):
    flag = True
    for j in range(n):
        if i == n - j - 1:
            print(1, end=" ")
            flag = False
        else:
            if flag:
                print(0, end=" ")
            else:
                print(2, end=" ")
    print()
