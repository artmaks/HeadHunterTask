# coding: utf-8

from itertools import count

# Посимвольный генератор строки состоящий из последовательных чисел
def char_generator():
    # Перечисляем последовательно числа
    for n in count():
        # Пробегаем по каждой букве в числе
        for char in str(n):
            yield char

# Найти первое вхождение
def find(number):
    number = str(number)            # Число
    generator = char_generator()    # Генератор последовательности
    
    index = 0
    # Посимвольно
    for current_char in generator:
        # Флаг для отслеживания состояния поиска подстроки
        complete = True
        # Пробегаем по символам нашего числа
        for number_char in number:
            # Если наш очередной символ равен символу генератора
            if current_char == number_char:
                # Генерируем следующий и продолжаем цикл
                current_char = generator.next()
                index += 1
            # Иначе символы отличаются, вхождения нет
            else:
                # Устанавливаем флаг поиска в False
                complete = False
                break

        # Если флаг не был переключен в False (вхождение не прервано)
        # Возвращаем индекс вхождения, прерываем функцию
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