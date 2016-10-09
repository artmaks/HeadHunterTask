# coding: utf-8

import numpy as np
from numpy import sum

# Проверяем, является ли клетка низиной.
# Если не является => False
# Если явлется => набор клеток являющихся низиной (частный случай, когда 1 клетка)
def isBottom(map, x, y, route):
    point = {'x': x, 'y': y}
    
    if point in route:
        return True
    
    route.append(point)
    
    if(x == 0 or x == map.shape[0] - 1): return False
    if(y == 0 or y == map.shape[1] - 1): return False
    
    if(map[x][y] == map[x + 1][y] and 'right' not in route and isBottom(map, x + 1, y, route) == False):
        return False
    if(map[x][y] == map[x][y - 1] and 'down' not in route and isBottom(map, x, y - 1, route) == False):
        return False
    if(map[x][y] == map[x - 1][y] and 'left' not in route and isBottom(map, x - 1, y, route) == False):
        return False
    if(map[x][y] == map[x][y + 1] and 'up' not in route and isBottom(map, x, y + 1, route) == False):
        return False
    
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
    rain_amount = 0
    old_sum = 0
    while sum(sum(island)) != old_sum:
        old_sum = sum(sum(island))
        for x in range(island.shape[0]):
            for y in range(island.shape[1]):
                res = isBottom(island, x, y, [])
                if(res):
                    amount = getMinimumAmount(island, res)
                    rain_amount += fillCells(island, amount, res)

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