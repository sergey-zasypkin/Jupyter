#Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

n = int(input('Enter number: ')) 

def sequence(n):

    return[round((1 + 1 / x)**x, 2) for x in range (1, n + 1)]   
        
print(sequence(n))

