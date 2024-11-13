def isCorrectRect():
    counter = 0 #показывает, в каком из прямоугольниов ошибка 
    
    class RectCorrectError(Exception):  #Класс для ошибки 
        pass


    for i in rectangles: #перебор всех прямоугольничков
        counter += 1
        try: 
            if i[0][0] >= i[1][0] or i[0][1] >= i[1][1]:
                raise RectCorrectError(f'Один из прямоугольников некорректный номер {counter}')
        except RectCorrectError as e:
            print(e)
            return False  

    return True  
