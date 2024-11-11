import math

numbers = int(input('Введите кол-во чисел: '))
for _ in range(numbers):
    number = float(input('Введите число: '))
    if number > 0:
        number = math.ceil(number)
        print(f'x = {number} log(x) = {math.log(number)}')
    else:
        number = math.floor(number)
        print(f'x = {number} exp(x) = {math.exp(number)}')