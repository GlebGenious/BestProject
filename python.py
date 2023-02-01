
chetnie_chisla = []
nechetnie_chisla = []
numbers = []
print('введите число, когда захотите закончить напишите viss')
while True:
    user_number = input('введите числа:')
    if user_number == 'viss':
        break
    number = int(user_number)
    numbers.append(user_number)
    if number % 2 == 0:
        chetnie_chisla.append(number)
    else:
        nechetnie_chisla.append(number)
print('число чётное', chetnie_chisla )
print('нечётные числа', nechetnie_chisla )
