def intersectionAreaMultiRect(rectangles):


    all_points = []  
    result = []

    class RectCorrectError(Exception):
        pass

    # Проверка на корректность прямоугольников
    for i in rectangles:
        if i[0][0] >= i[1][0] or i[0][1] >= i[1][1]:
            raise RectCorrectError('Один из прямоугольников некорректный')

    # Генерация всех точек для каждого прямоугольника
    for rect in rectangles:
        points = [(x, y) for x in range(int(rect[0][0]), int(rect[1][0]))   for y in range(int(rect[0][1]), int(rect[1][1]))]
        all_points.extend(points)  

    #Уникальные точки
    unique = set(all_points)

    # сколько раз каждая точка встречается
    for point in unique:
        count = all_points.count(point)
        if count == 2:  
            result.append(point)
    return len(result)

rectangles = [
    [(-3, 1), (9, 10)],
    [(-7, 0), (13, 12)],
    [(0, 0), (5, 5)],
    [(2, 2), (7, 7)]
]

result = intersectionAreaMultiRect(rectangles)
print("Площадь пересечения:", result)
