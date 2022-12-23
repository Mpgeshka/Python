list = [4, 7, 1, 10, 3]
print(list)

sum = 0
for i in range(len(list)):
    if i %  2 != 0:
        sum = sum + list[i]
print(f'Сумма элементов на нечетных позициях {list} равна', sum)