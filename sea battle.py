import random

# Ввод размера поля
размер_поля = int(input("Введите размер поля: "))

# Ввод количества кораблей
количество_кораблей = int(input("Введите количество кораблей: "))

# Инициализация игрового поля
поле = [['~' for _ in range(размер_поля)] for _ in range(размер_поля)]

# Генерация кораблей компьютера
корабли_компьютера = []
for _ in range(количество_кораблей):
    длина_корабля = random.randint(1, 4)
    ряд_корабля = random.randint(0, размер_поля - 1)
    колонка_корабля = random.randint(0, размер_поля - 1)
    ориентация = random.choice(['горизонтальная', 'вертикальная'])
    if ориентация == 'горизонтальная':
        if колонка_корабля + длина_корабля > размер_поля:
            колонка_корабля = размер_поля - длина_корабля
        for i in range(длина_корабля):
            корабли_компьютера.append((ряд_корабля, колонка_корабля + i))
    else:
        if ряд_корабля + длина_корабля > размер_поля:
            ряд_корабля = размер_поля - длина_корабля
        for i in range(длина_корабля):
            корабли_компьютера.append((ряд_корабля + i, колонка_корабля))
# Игра
количество_попыток = 0
while True:
    # Печать игрового поля с нумерацией строк и столбцов
    print('   ' + ' '.join(str(i) for i in range(размер_поля)))
    for i, row in enumerate(поле):
        номер_ряда = str(i).rjust(2)
        print(номер_ряда + ' ' + ' '.join(row))

    # Ввод предположения пользователя
    предположенный_ряд_или_gg = input("Предполагаемая строка (0-{}), или напишите gg, если хотите сдаться: ".format(размер_поля - 1))

    # Проверка команды "gg" для сдачи и завершения игры
    if предположенный_ряд_или_gg == 'gg':
        print("Вы сдались. Корабли компьютера:")
        for корабль in корабли_компьютера:
            поле[корабль[0]][корабль[1]] = 'X'
        break

    предположенная_колонка = int(предположенный_ряд_или_gg)

    # Ввод предположения пользователя
    предположенный_колонка_или_gg = input("Предполагаемая колонка (0-{}), или напишите gg, если хотите сдаться: ".format(размер_поля - 1))

    # Проверка команды "gg" для сдачи и завершения игры
    if предположенный_колонка_или_gg == 'gg':
        print("Вы сдались. Корабли компьютера:")
        for корабль in корабли_компьютера:
            поле[корабль[0]][корабль[1]] = 'X'
        break

    предположенный_ряд = int(предположенный_колонка_или_gg)

    # Проверка попадания или промаха
    if (предположенный_ряд, предположенная_колонка) in корабли_компьютера:
        поле[предположенный_ряд][предположенная_колонка] = '*'
        print("Попадание!")
    else:
        поле[предположенный_ряд][предположенная_колонка] = '-'
        print("Промах!")

    # Проверка окончания игры
    количество_попыток += 1
    if set(корабли_компьютера).issubset(
            set([(i, j) for i in range(размер_поля) for j in range(размер_поля) if поле[i][j] == 'X'])):
        print("Вы выиграли за", количество_попыток, "попыток!")
        break

# Печать игрового поля с кораблями компьютера
print("Корабли компьютера:")
for корабль in корабли_компьютера:
    поле[корабль[0]][корабль[1]] = 'X'

# Печать игрового поля с нумерацией строк и столбцов и кораблями компьютера
print('   ' + ' '.join(str(i) for i in range(размер_поля)))
for i, row in enumerate(поле):
    номер_ряда = str(i).rjust(2)
    print(номер_ряда + ' ' + ' '.join(row))
