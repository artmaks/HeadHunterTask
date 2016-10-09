# coding: utf-8

import numpy as np
from numpy import sum

# Проверяем, является ли клетка низиной
# И все ее соседи с той же высотой (функция рекурентная)
# Если не является (вода уходит) => False
# Если явлется (вода остается) => набор клеток являющихся низиной (частный случай, когда 1 клетка)
def isBottom(map, x, y, route):
    point = {'x': x, 'y': y}

    # Точка останова рекурсии
    if point in route:
        return True

    # Добавляем точку в историю посещения
    route.append(point)

    # Проверка на пограничные значения (около моря)
    if(x == 0 or x == map.shape[0] - 1): return False
    if(y == 0 or y == map.shape[1] - 1): return False

    # Проверка соседей точки
    # Если есть точка одинаковой высоты, то проверяем ее рекурентно
    # Если есть соседи ниже точки (рекурентно) => прерываем проверку (False)
    if(map[x][y] == map[x + 1][y] and 'right' not in route and isBottom(map, x + 1, y, route) == False):
        return False
    if(map[x][y] == map[x][y - 1] and 'down' not in route and isBottom(map, x, y - 1, route) == False):
        return False
    if(map[x][y] == map[x - 1][y] and 'left' not in route and isBottom(map, x - 1, y, route) == False):
        return False
    if(map[x][y] == map[x][y + 1] and 'up' not in route and isBottom(map, x, y + 1, route) == False):
        return False


    # Если мы прошли проверки выше, значит
    # точки равные нашей нам подходят
    # проверяем, что все соседи хотя бы не больше
    # возвращаем весь путь, проделанный рекурсией
    if(map[x][y] <= map[x + 1][y] and
       map[x][y] <= map[x - 1][y] and
       map[x][y] <= map[x][y + 1] and 
       map[x][y] <= map[x][y - 1]):
        return route
    else:
        return False
    

# Вернуть всех соседей для клетки
def getNeighbors(p):
    neighbors = [{'x' : p['x'] + 1, 'y' : p['y']}, 
                 {'x' : p['x'] - 1, 'y' : p['y']}, 
                 {'x' : p['x'], 'y' : p['y'] + 1}, 
                 {'x' : p['x'], 'y' : p['y'] -1}]
    return neighbors


#Находит минимального соседа для группы клеток (место через которое утекает вода)
def getMinimumAmount(map, points):
    data = []
    for p in points:
        for neighbor in getNeighbors(p):
            if neighbor not in points:
                data.append(neighbor)
        
    data = [island[i['x']][i['y']] for i in data]
    current_height = map[points[0]['x']][points[0]['y']]
    return np.min(data) - current_height

#Заполняет указанные клетки, указанным количеством воды
def fillCells(map, amount, points):
    for p in points:
        map[p['x']][p['y']] += amount
        
    return amount * len(points)

# Главный метод для подсчета осадков
def rain(island):
    rain_amount = 0 # кол-во осадков
    old_sum = 0     # переменная для отслеживания изменений на острове

    # Пока сумма высот на острове меняется
    while sum(sum(island)) != old_sum:

        # Записываем новую сумму высот
        old_sum = sum(sum(island))

        # Пробегаем по клеткам острова последовательно
        for x in range(island.shape[0]):
            for y in range(island.shape[1]):
                # Проверяем состояние ячейки
                res = isBottom(island, x, y, [])
                # Если ячейка - низменность
                if(res):
                    amount = getMinimumAmount(island, res)          # Находим максимум, который мы можем добавить
                    rain_amount += fillCells(island, amount, res)   # Заполняем ячейки, добавляем результат в rain_amount

    return rain_amount



stdin = open("stdin", "r")
stdout = open("stdout", "r+")
stdout.seek(0)
stdout.truncate()

island_count = int(stdin.readline())
for i in range(island_count):
    island = []
    size = [int(i) for i in stdin.readline().split(' ')]
    for i in range(size[0]):
        numbers = [int(i) for i in stdin.readline().split(' ')]
        island.append(numbers)

    island = np.array(island)

    stdout.write(str(rain(island)) + '\n')

stdin.close()
stdout.close()