list = [5,4,8,3,1]
print(list,'==>')

def mult(list):
    mult = []
    for i in range((len(list)+1)//2):
        mult.append(list[i]*list[len(list)-1-i])
    return mult
print(mult(list))