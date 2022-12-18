a, b, c = 1, 2, 3
print('a: {} b: {} c: {}'.format(a, b, c))
range(*(1,5,2))

a = int(input('Введите \nа: '))
b = int(input('Введите \nb: '))
c = a + b
print('{} + {} = {}'.format(a, b, c))

exp1 = 2**3 - 10 % 5 + 2*3
exp2 = 2**3 - 10 / 5 + 2*3
print(exp1) # 14.0 или 14
print(exp2) # 12.0 или 12


a, b, c = 1, 2, 3
# a: 1 b: 2 c: 3
print('a: {} b: {} c: {}'.format(a, b, c))
range(*(1,5,2))

username = input('Введите имя: ')
if(username == 'Маша'):
 print('Ура, это же МАША!');
else:
 print('Привет, ', username);


username = input('Введите имя: ')
if username == 'Маша':
     print('Ура, это же МАША!')
elif username == 'Марина':
     print('Я так ждала Вас, Марина!')
elif username == 'Ильнар':
     print('Ильнар - топ)')
else:
     print('Привет, ', username)


original = 23
inverted = 0
while original != 0:
 inverted = inverted * 10 + (original % 10)
 original //= 10
print(inverted)


original = 25
inverted = 0
while original != 0:
 inverted = inverted * 10 + (original % 10)
 original //= 10
else:
 print('Пожалуй')
 print('хватит )')
print(inverted)

for i in 1, -2, 3, 14, 5:
    print(i)

r = range(100, 0, -20)          # range(100, 0, -20)
for i in r:
    print(i)
# 100 80 60 40 20
for i in range(5):
    print(i)
# 0 1 2 3 4

line = ""
for i in range(5):
    line = ""
    print(line)
for j in range(5):
    line += "*"
    print(line)
text = 'съешь ещё этих мягких французских булок'
print(len(text)) # 39
print('ещё' in text) # True
print(text.isdigit()) # False
print(text.islower()) # True
print(text.replace('ещё','ЕЩЁ')) #
for c in text:
    print(c)


text = 'съешь ещё этих мягких французских булок'
print(text[0]) # c
print(text[1]) # ъ
print(text[len(text)-1]) # к
print(text[-5]) # б
print(text[:]) # print(text)
print(text[:2]) # съ
print(text[len(text)-2:]) # ок
print(text[2:9]) # ешь ещё
print(text[6:-18]) # ещё этих мягких
print(text[0:len(text):6]) # сеикакл
print(text[::6]) # сеикакл
text = text[2:9] + text[-5] + text[:2] # ...