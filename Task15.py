age = int(input('Введите свой возраст '))
numbers = list(range(1, age + 1))
if age % 2 == 0:
    numbers.pop(0)
print(numbers[::2])
