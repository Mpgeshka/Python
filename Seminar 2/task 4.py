from random import Random, randint

N = int(input('Введите количество элементов:  '))
numbers = []
for i in range(N):
    numbers.append(randint(-N, N + 1))

print(numbers)

def get_numbers(numbers):
    count =0
    for element in numbers:
        count +=1
    return count

x = int(input('Введите позицию первого элемента: '))
y = int(input('Введите позицию второго элемента: '))

for i in range(len(numbers)):
    mult = numbers[x -1]*numbers[y - 1]
print(f'Произведение элементов: {numbers[x -1]} * {numbers[y -1]} =', mult)