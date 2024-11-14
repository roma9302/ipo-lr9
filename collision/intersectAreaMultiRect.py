from collision.CorrectRec import isCorrectRect, RectCorrectError

def intersectionAreaMultiRect(rectangles):
    all_points = []  
    result = []
    try:
        isCorrectRect(rectangles)
    except RectCorrectError as e:
        print(e)
        return 0  

    # из флот в инт и перебор этих точек
    for rect in rectangles:
        points = [(int(x), int(y)) for x in range(int(rect[0][0] * 10), int(rect[1][0] * 10)) 
                                                        for y in range(int(rect[0][1] * 10), int(rect[1][1] * 10))]
        all_points.extend(points)  

    # Уникальные точки
    unique = set(all_points)

    # Сколько раз каждая точка встречается
    for point in unique:
        count = all_points.count(point)
        if count >= 2 and point not in result:  
            result.append(point)
    
    # Площадь пересечения 
    return len(result) / 100


