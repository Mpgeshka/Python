list = [1.6, 1.1, 3.8, 5.9, 10.55]
print(list)

def dif(list):
    dif_max_min =[]
    for i in range(len(list)):
        dif_max_min.append(list[i]%1)
    return max(dif_max_min) - min(dif_max_min)
print(round(dif(list),2))