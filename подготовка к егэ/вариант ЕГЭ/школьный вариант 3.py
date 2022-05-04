file = open('zadanie_17.txt', 'r')
sp = map(int, file.read().strip().split('\n'))
cnt = 0
ans = 0
for num in sp:
    if num % 5 == 0 and num % 6 != 0 and num % 10 != 0 and num % 15 != 0 and num % 16 != 0:
        cnt += 1
        if ans == 0 or ans < num:
            ans = num
print(cnt, ans)