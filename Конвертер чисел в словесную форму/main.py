first_razryad = {0: "ноль", 1: "один", 2: "два", 3: "три", 4: "четыре", 5: "пять",
                 6: "шесть", 7: "семь", 8: "восемь", 9: "девять"}
dict_11_to_19 = {11: "одиннадцать", 12: "двенадцать", 13: "тринадцать", 14: "четырнадцать",
                 15: "пятнадцать", 16: "шестнадцать", 17: "семнадцать",
                 18: "восемнадцать", 19: "девятнадцать",  10: "десять"}
second_razryad = {1: "десять", 2: "двадцать", 3: "тридцать", 4: "сорок", 5: "пятьдесят",
                 6: "шестьдесят", 7: "семьдесят", 8: "восемьдесят", 9: "девяносто"}
third_razryad = {1: "сто", 2: "двести", 3: "триста", 4: "четыреста", 5: "пятьсот",
                 6: "шестьсот", 7: "семьсот", 8: "восемьсот", 9: "девятьсот"}


def convert(number):
    if len(str(number)) == 1:
        return first_razryad.get(number)
    elif 10 <= number <= 19:
        return dict_11_to_19.get(number)
    elif 20 <= number <= 99:
        if number % 10 == 0:
            return second_razryad.get(number // 10)
        return ' '.join([second_razryad.get(number // 10), first_razryad.get(number % 10)])
    elif 100 <= number <= 999:
        if number % 100 == 0:
            return third_razryad.get(number // 100)
        st = list()
        st.append(third_razryad.get(number // 100))
        if number % 100 in dict_11_to_19:
            st.append(dict_11_to_19.get(number % 100))
        elif number % 100 >= 20:
            st.append(second_razryad.get(number % 100 // 10))
            if number % 10 != 0:
                st.append(first_razryad.get(number % 10))
        else:
            st.append(first_razryad.get(number % 10))
