emails = {'nosu.edu': ['timyr', 'joseph', 'svetlana.gaeva', 'larisa.mamuk'],
          'gmail.com': ['ruslan.chaika', 'rustam.mini', 'stepik-best'],
          'msu.edu': ['apple.fruit', 'beegeek', 'beegeek.school'],
          'yandex.ru': ['surface', 'google'],
          'hse.edu': ['tomas-henders', 'cream.soda', 'zivert'],
          'mail.ru': ['angel.down', 'joanne', 'the.fame.moster']}
ans = list()
for key, value in emails.items():
    for name in value:
        ans.append(name + '@' + key)
print(*sorted(ans))