import random

length = int(input())    # длина пароля
ans = ''
while len(ans) < length:
    if ans == '':
        if random.randint(0, 2) == 0:
            ans += chr(random.randint(65, 90)).lower()
            ans += chr(random.randint(65, 90))
        else:
            ans += chr(random.randint(65, 90))
            ans += chr(random.randint(65, 90)).lower()
    else:
        if random.randint(0, 2) == 0:
            ans += chr(random.randint(65, 90)).lower()
        else:
            ans += chr(random.randint(65, 90))
print(ans)