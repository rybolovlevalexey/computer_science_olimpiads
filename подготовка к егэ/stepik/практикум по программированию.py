is_non_negative_num = lambda x: (type(x) == int or type(x) == float) and int(x) >= 0
num = '10.45'
print(type(num) == int, type(num) == float, float(num) >= 0)