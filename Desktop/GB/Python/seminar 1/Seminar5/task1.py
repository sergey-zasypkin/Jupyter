# Напишите программу, удаляющую из текста все слова, содержащие ""абв""

my_text = 'Напишите программу, удаляющую из текста все слова, содержащие абв и еже с ними абвгдешки и тому подобные фбвешки'

def delete(my_text):
    my_text = list(filter(lambda x: 'абв' not in x, my_text.split()))
    return " ".join(my_text)

my_text = delete(my_text)
print(my_text)