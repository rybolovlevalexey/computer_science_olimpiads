def pretty_print(data, side='-', delimiter='|'):
    ans = delimiter + " " + f" {delimiter} ".join(list(map(str, data))) + " " + delimiter
    print(" " + side * (len(ans) - 2) + " \n" + ans + "\n" + " " + side * (len(ans) - 2) + " ")
