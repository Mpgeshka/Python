import random
list = [random.randint(0,26) for i in range (20)]
print(list)
new_list =[]
[new_list.append(i) for i in list if i not in new_list ]
print(new_list)