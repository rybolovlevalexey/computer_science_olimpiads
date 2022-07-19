numbers = [1, 2, 3, 4, 5]
print(*enumerate(numbers))
for count, item in enumerate(numbers):
    if count % 2 == 0:
        print(item)
print(count)