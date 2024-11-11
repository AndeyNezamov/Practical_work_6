import math
file = int(input('Укажите размер файла для скачивания: '))
speed = int(input('Какова скорость вашего соединения: '))
time = math.ceil(file / speed)
percent = math.ceil(speed / file * 100)
total = speed

for i in range(1, time+1):
  print('Прошло', i, 'сек. Скачено:', total, 'из', file, '(', percent, '%)')
  total += speed
  percent += math.ceil(speed / file * 100)
  if total > file:
    total = file
  if percent > 100:
    percent = 100