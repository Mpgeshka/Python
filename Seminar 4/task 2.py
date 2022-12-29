a = int(input('Введите число: '))
list =[]
for i in range(1,a+1):
    if(a%i==0):
      list.append(i)
print(f'{a} = {list}')