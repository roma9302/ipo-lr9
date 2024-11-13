from collision.CorrectRec import isCorrectRect , RectCorrectError
def intersectionAreaMultiRect(rectangles):

    all_points = []  
    result = []
    try:
        isCorrectRect(rectangles)
    except RectCorrectError as e:
        print(e)
        return 0  
    #  все точки для каждого прямоугольника
    for rect in rectangles:
        points = [(x, y) for x in range(int(rect[0][0]), int(rect[1][0]))   for y in range(int(rect[0][1]), int(rect[1][1]))]
        all_points.extend(points)  

    #Уникальные точки
    unique = set(all_points)

    # сколько раз каждая точка встречается
    for point in unique:
        count = all_points.count(point)
        if count >= 2 and point not in result:  
            result.append(point)
    return len(result)

