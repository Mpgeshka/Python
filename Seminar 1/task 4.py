n = int(input('Введите номер четверти: '))
if n < 1 or n > 4:
     print('Ошибка! Пожалуйста, измените ввод номера четверти!')
elif n == 1: print('x > 0 and y > 0')
elif n == 2: print('x < 0 and y > 0')
elif n == 3: print('x < 0 and y < 0')
elif n == 4: print('x > 0 and y < 0')