from collision.CorrectRec import isCorrectRect , RectCorrectError
from itertools import combinations

def intersectionAreaMultiRect(rectangles):
    
    # получение координат пересечения двух и более прямоугольников
    def get_intersection(rects):
        x1 = max(rect[0][0] for rect in rects)
        y1 = max(rect[0][1] for rect in rects)
        x2 = min(rect[1][0] for rect in rects)
        y2 = min(rect[1][1] for rect in rects)
        if x1 < x2 and y1 < y2:
            return [(x1, y1), (x2, y2)]
        return None
    
    # вычисление площади прямоугольника
    def area(rect):
        if not rect:
            return 0
        width = rect[1][0] - rect[0][0]
        height = rect[1][1] - rect[0][1]
        return width * height

    # проверка корректности входных данных
    try:
        isCorrectRect(rectangles)
    except RectCorrectError as e:
        print(e)
        return 0

    total_area = 0 # искомая площадь
    all_intersections = [] #  все пересечений двух фигур каждая с каждой
    
    # вычисляем суммарную площадь всех пересечений двух фигур
    for combination in combinations(rectangles, 2):
            intersection = get_intersection(combination)
            if intersection:
                all_intersections.append(intersection)
    
    # вычисляем итоговую площадь пересечений двух и более фигур
    # формула включений-исключений
    for k in range(1, len(all_intersections) + 1):
        sign = (-1) ** (k + 1)  # Чередование знаков
        for combination in combinations(all_intersections, k):
            intersection = get_intersection(combination)
            total_area += sign * area(intersection)
    return total_area

