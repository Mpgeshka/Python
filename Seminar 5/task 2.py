from random import randint

candies = 500
print(f'{candies} всего конфет')
count = randint(1, 2)
while candies > 0:
    count += 1
    if count % 2 == 0:
        if count == 2:
            print('ходит бот')
            quantity = 20
            print(f'конфет изымаете бот {quantity}')
        else:
            print('ходит бот')
            quantity = 29 - quantity
            print(f'конфет изымаете бот {quantity}')
    else:
        print('ходит игрок')
        quantity = int(input('Введите число конфет которое изымаете - '))
    if 0 < quantity < 29:
        candies -= quantity
        print(f'конфет осталось - {candies}')
    else:
        print('Вы ввели некоректное кол-во конфет, введите число от 1 до 28')
        count -= 1

if count % 2 == 0:
    print('победил бот')
else:
    print('победил игрок')
