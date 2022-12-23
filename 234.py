with open('file.txt', 'w') as data:
    data.write('line 1\n')
    data.write('line 2\n')
colors = ['red', 'green', 'blue']
data = open('file.txt', 'a')
data.writelines(colors) # разделителей не будет
data.close()
path = 'file.txt'
data = open(path, 'r')
for line in data:
    print(line)
data.close()


def f(x):
     return x**2
def f(x):
 if x == 2:
    return 'Целое'
 elif x == 5.3:
    return 53
 else:
    return
print(f(2)) # Целое
print(f(5.3)) # 23
print(f(28)) # None
print(type(f(2))) # str
print(type(f(5.3))) # int
print(type(f(28))) # NoneType