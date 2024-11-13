def intersectionAreaRect(rectangles):

    area = 0  

    #корректность 
    try:
        isCorrectRect(rectangles)
    except RectCorrectError as e:
        print(e)
        return 0  

    n = len(rectangles) #колво прямоугольничков 

    for i in range(n):
        for j in range(i + 1, n):
            # Границы первого прямоугольника
            x1, y1 = rectangles[i][0]
            x2, y2 = rectangles[i][1]

            # Границы второго прямоугольника
            x3, y3 = rectangles[j][0]
            x4, y4 = rectangles[j][1]

            # Границы пересечения
            left = max(x1, x3)
            top = min(y2, y4)
            right = min(x2, x4)
            bottom = max(y1, y3)

            # Ширина и высота пересечения
            width = right - left
            height = top - bottom

            # площадь пересечения
            if width > 0 and height > 0:
            	return width * height
            else:
            	return False
