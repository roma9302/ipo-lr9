from .CorrectRec import isCorrectRect, RectCorrectError


def isCollisionRect(rectangles):
    try:
        isCorrectRect(rectangles)
    except RectCorrectError as e:
        print(e)
        return False
        
    n = len(rectangles)
    
    for i in range(n):
        for j in range(i + 1, n):
            # Первый прямоугольник
            x1, y1 = rectangles[i][0]
            x2, y2 = rectangles[i][1]

            # Второй прямоугольник
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

            # Проверяем пересечение
            if width > 0 and height > 0:
                return True  

    return False  
