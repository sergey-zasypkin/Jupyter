# Напишите программу, удаляющую из текста все слова, содержащие "абв"
text = input('Введите искомые символы: ')
with open('text.txt', 'r', encoding = 'utf_8') as file:
    list = list(filter(lambda x: text not in x, file.read().split()))

print (list)