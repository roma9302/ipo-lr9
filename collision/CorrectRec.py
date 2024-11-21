class RectCorrectError(Exception):  # Класс для ошибки 
    pass

def isCorrectRect(rectangles):
    counter = 0  # показывает в каком из прямоугольников ошибка 
    
    for i in rectangles:  # перебор всех прямоугольников
        counter += 1
        if i[0] >= i[1]or i[0]>= i[1]:
            raise RectCorrectError(f'Один из прямоугольников некорректный номер {counter}')

    return True   
