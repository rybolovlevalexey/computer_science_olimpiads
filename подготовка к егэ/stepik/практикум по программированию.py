class multifilter:
    def judge_half(pos, neg):
        # допускает элемент, если его допускает хотя бы половина фукнций (pos >= neg)
        if pos >= neg:
            return True
        return False

    def judge_any(pos, neg):
        # допускает элемент, если его допускает хотя бы одна функция (pos >= 1)
        if pos >= 1 and neg is not None:
            return True
        return False

    def judge_all(pos, neg):
        # допускает элемент, если его допускают все функции (neg == 0)
        if neg == 0 and pos is not None:
            return True
        return False

    def __iter__(self):
        # возвращает итератор по результирующей последовательности
        result = list()
        for i in range(len(self.sp)):
            p, n = self.pn_sp[i]
            elem = self.sp[i]
            if self.judge(p, n):
                result.append(elem)
        return iter(result)

    def __init__(self, iterable, *funcs, judge=judge_any):
        self.sp = iterable
        self.all_funcs = funcs
        self.judge = judge
        self.pn_sp = list()
        for elem in self.sp:
            p = 0
            n = 0
            for func in self.all_funcs:
                if func(elem):
                    p += 1
                else:
                    n += 1
            self.pn_sp.append([p, n])


def mul2(x):
    return x % 2 == 0

def mul3(x):
    return x % 3 == 0

def mul5(x):
    return x % 5 == 0


a = [i for i in range(31)] # [0, 1, 2, ... , 30]

#print(list(multifilter(a, mul2, mul3, mul5)))
# [0, 2, 3, 4, 5, 6, 8, 9, 10, 12, 14, 15, 16, 18, 20, 21, 22, 24, 25, 26, 27, 28, 30]

print(list(multifilter(a, mul2, mul3, mul5, judge=multifilter.judge_half)))
# [0, 6, 10, 12, 15, 18, 20, 24, 30]

print(list(multifilter(a, mul2, mul3, mul5, judge=multifilter.judge_all)))
# [0, 30]