def intersectionAreaMultiRect(rectangles):
    isCorrectRect(rectangles) 

    intersections = []
    
    # пересечения между всеми парами
    for i in range(len(rectangles)):
        for j in range(i + 1, len(rectangles)):
            x1 = max(rectangles[i][0][0], rectangles[j][0][0])
            y1 = max(rectangles[i][0][1], rectangles[j][0][1])
            x2 = min(rectangles[i][1][0], rectangles[j][1][0])
            y2 = min(rectangles[i][1][1], rectangles[j][1][1])
            
            if x1 < x2 and y1 < y2:
                inter = (x1, y1), (x2, y2)  # ху пересечений
                intersections.append(inter)

    # уникальная площадь
    unique_intersections = set(intersections)
    
    
    #площадь 
    area = 0
    for rect in unique_intersections:
        width = rect[1][0] - rect[0][0]
        height = rect[1][1] - rect[0][1]
        area += width * height

    return area



#возвращение площади/ошибки
try:
    result = intersectionAreaMultiRect(rectangles)
    print(f"Уникальная площадь пересечения: {result}")
except RectCorrectError as e:
    print(e)
