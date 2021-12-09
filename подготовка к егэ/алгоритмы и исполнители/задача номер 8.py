for i in range(-1000, 1000):
   x = i
   x0 = x
   N = 0
   while x>0:
      d = x % 3
      N = 10*N + d
      x = x // 3
   N += x0
   if len(str(abs(N))) == 4:
      print(i, N)