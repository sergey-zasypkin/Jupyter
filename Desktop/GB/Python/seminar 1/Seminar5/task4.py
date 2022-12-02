# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных

def RLE_encode(tx):
    res = ''
    count = 1
    for i in range(len(tx)-1):
        if tx[i]!=tx[i+1]:
            res+=str(count) + tx[i]
            count = 1
        else: count+=1
    res+=str(count) + tx[len(tx)-1]
    return res

def RLE_decode(tx):
    res = ''
    count = ''
    for i in range(len(tx)-1):
        if tx[i].isdigit():
            count+=tx[i]
        else:
            res+=tx[i]*int(count)
            count = ''
    res+=tx[len(tx)-1]*int(count)
    return res

with open(r'C:\Users\Sergey Zasypkin\Desktop\GB\Python\seminar 1\Seminar5\input.txt','r') as fl:
    dt = fl.read().split('\n')
    enc = dt[0]
    dec = dt[1]

with open(r'C:\Users\Sergey Zasypkin\Desktop\GB\Python\seminar 1\Seminar5\output.txt','w') as fl1:
    fl1.write(RLE_encode(enc))
    fl1.write("\n")
    fl1.write(RLE_decode(dec))