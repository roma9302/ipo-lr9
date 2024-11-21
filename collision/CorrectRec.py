class RectCorrectError(Exception):  # Класс для ошибки 
    pass

def isCorrectRect(rectangles):
    counter = 0  # показывает в каком из прямоугольников ошибка 
    
    for i in rectangles:  # перебор всех прямоугольников
        counter += 1
        if i[0][0] >= i[1][0] or i[0][1] >= i[1][1]:
            raise RectCorrectError(f'Один из прямоугольников некорректный номер {counter}')

    return True
