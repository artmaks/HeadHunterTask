# coding: utf-8

from itertools import count

# Посимвольный генератор строки состоящий из последовательных чисел
def char_generator():
    for n in count():
        for char in str(n):
            yield char

# Найти первое вхождение
def find(number):
    number = str(number)
    generator = char_generator()
    
    index = 0
    for current_char in generator:
        complete = True
        for number_char in number:
            if current_char == number_char:
                current_char = generator.next()
                index += 1
            else:
                complete = False
                break
                
        if complete == True:
            return index - len(number)
        
        index += 1

stdout = open("stdout", "r+")
stdout.seek(0)
stdout.truncate()

with open('stdin') as stdin:
    for line in stdin:
        res = find(int(line))
        stdout.write(str(res) + '\n')

stdout.close()