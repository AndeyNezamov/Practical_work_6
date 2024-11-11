import math

r = float(input('Введите радиус случайной планеты: '))
earth = 1.08321 * (10 ** 12)
v = round(4 * math.pi / 3 * (r ** 3),3)

if earth > v:
    print(f'Объем планеты Земля больше в {round(earth/ v, 3)} раз')
else:
    print(f'Объем планеты Земля меньше в {round(v / earth, 3)} раз')
